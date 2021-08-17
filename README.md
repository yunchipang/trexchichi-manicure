# trexchichi-manicure

### Video Demo:  <URL HERE>
### Description:

This project (trexchichi-manicure) is a web-app inspired by the manicure studio I visit regularly. The web-app is built with Flask and a PostgreSQL database, hosted on Heroku. The main goal is to reduce human error when trying to find customer information in huge binders, and save time.

### functions:
- log in: the manicure studio has 1 admin only. once a customer completes a beauty treatment, the admin logs in to the portal and record the payment. if he/she is a new customer, the admin lets he/she register first.
- log out: simply clears the session.
- transaction: when a cusomter completes a manicure session (or any other treatment), the admin goes to `/transaction` and record the information.
- top up: the studio allows regular customers to top-up their account in advance. When they come for a treatment, they do not have to pay cash, since the amount gets deducted from the stored value.
- user: a customer can get their personal information and past transactions from `/user`.
- register: a new customer should always register for an account first before accessing any of the service mentioned above.

### database
- table1: `users`
- table2: `transactions`
- table3 `topups`

### walk-through
1. log in with username: `username` & password: `password`.
2. head to `/register`, input username, phone number, email & birthday.
3. head to `/topup`, enter your registered phone number and how much you want to store.
4. pretend that you have completed a manicure session, then head to `/transaction` and record your transaction.
5. then head back to `/user`, check your account status & previous transactions using your phone number.