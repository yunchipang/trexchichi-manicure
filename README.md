# trexchichi-manicure

- url: [https://trexchichi-manicure.herokuapp.com/](https://trexchichi-manicure.herokuapp.com/) update: the heroku site is no longer available after they ended the free hosting service. still trying to find a replacement!
- video demo:  [https://youtu.be/2SF4djZxSsE](https://youtu.be/2SF4djZxSsE)

### overview 

**trexchichi-manicure** is a web-app inspired by the manicure studio I visit regularly. The main goal of the project is to reduce human error when trying to find customer information in huge binders, and save time. The web-app is built with Flask and a PostgreSQL database, hosted on Heroku.

##### 1. functions:
- **log in**: the manicure studio has 1 admin only. Once a customer completes a beauty treatment, the admin logs in to the portal and records the payment.
- **log out**: simply clears the session.
- **transaction**: when a cusomter completes a manicure session (or any other treatment), the admin goes to `/transaction` and record the information.
- **top up**: the studio allows regular customers to top-up their account in advance. When they come for a treatment, they do not have to pay in cash, since the amount gets deducted from the stored value.
- **user**: a customer can get their personal information and past transactions from `/user`.
- **register**: a new customer should always register for an account first before accessing any of the service mentioned above.

##### 2. database
- **table1**: `users`
- **table2**: `transactions`
- **table3** `topups`

### walk-through
1. log in with username: `username` & password: `password`.
2. head to `/register`, create a new user with your own information.
3. head to `/topup`, enter your registered phone number and how much money you want to store.
4. pretend that you have completed a beauty treatment (in any category), then head to `/transaction` and record your transaction.
5. then head back to `/user`, check your account status & previous transactions using your phone number.
