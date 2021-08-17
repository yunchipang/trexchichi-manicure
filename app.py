import os
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask import session, redirect
from functools import wraps
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///'+ os.path.join(basedir, 'manicure.db')
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)

def login_required(f):
    '''
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username') is None:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username:
            return render_template('login.html', message='must provide username')
        elif not password:
            return render_template('login.html', message='must provide password')
        
        # todo - admin username & password are hardcoded now - try to fix this
        if username == 'username' and password == 'password':
            session['username'] = username
            return redirect('/')
        return render_template('login.html', message='incorrect username and/or password. please try again.')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/transaction', methods=['GET', 'POST'])
@login_required
def transaction():
    from models import User, Transaction

    if request.method == 'POST':
        phone_number = request.form['phone_number']
        amount = request.form['amount']
        category = request.form['category']
        details = request.form['details']
        
        if phone_number == '' or amount == '' or category == '' or details == '':
            return render_template('index.html', message='please enter required fields.')
        
        user = User.query.filter_by(phone_number=phone_number).first()
        if user is None:
            return render_template('index.html', message='the customer does not exist, please register first.')
        if int(amount) > user.cash:
            return render_template('index.html', message='payment exceeds current value, please top-up first.')
        data = Transaction(user_id=user.id, amount=amount, category=category, details=details)
        db.session.add(data)
        # update user.cash
        user.cash -= int(amount)

        db.session.commit()
        return render_template('success.html', action='transaction')
    return render_template('transaction.html')


@app.route('/topup', methods=['GET', 'POST'])
@login_required
def topup():
    from models import User, Topup

    if request.method == 'POST':
        phone_number = request.form['phone_number']
        amount = request.form['amount']

        if phone_number == '' or amount == '':
            return render_template('topup.html', message='please enter required fields.')
        if int(amount) > 10000:
            return render_template('topup.html', message='the limit of single top-up is $10000')

        user = User.query.filter_by(phone_number=phone_number).first()
        if user is None:
            return render_template('topup.html', message='the customer does not exist, please register first.')
        db.session.add(Topup(user_id=user.id, amount=amount))
        # update user.cash
        user.cash += int(amount)
        db.session.commit()

        return render_template('success.html', action='top up record')
    return render_template('topup.html')


@app.route('/user', methods=['GET', 'POST'])
@login_required
def user():
    from models import User, Transaction

    if request.method == 'POST':
        user = User.query.filter_by(phone_number=request.form.get('phone_number')).first()
        if user is None:
            return render_template('user.html', message='the customer does not exist, please try again.')
        # customer info

        # transaction history
        transaction = Transaction.query.filter_by(user_id=user.id).order_by(Transaction.datetime.desc()).all()

        return render_template('user.html', user=user, transaction=transaction)
    return render_template('user.html')

@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    from models import User

    if request.method == 'POST':
        username = request.form['username']
        phone_number = request.form['phone_number']
        email = request.form['email']
        birthday = request.form['birthday']

        if username == '' or phone_number == '' or email == '' or birthday == '':
            return render_template('register.html', message='please enter all required fields.')
        if len(phone_number) != 10:
            return render_template('register.html', message='please enter a 10-digit number.')

        try:
            user = User(username=username, phone_number=phone_number, email=email, birthday=datetime.strptime(request.form['birthday'], '%Y-%m-%d').date())
            db.session.add(user)
            db.session.commit()
            return render_template('success.html', action='registration')
        # if username/phone_number/email duplicates with existing ones
        except IntegrityError:
            return render_template('register.html', message='the username is already being used, please try again. if you have registered before, please try logging in.')
    
    return render_template('register.html')

if __name__ == '__main__':
    #app.debug = True
    app.run()