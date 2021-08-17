# trexchichi-manicure
#### Video Demo:  <URL HERE>
#### Description:

This project (trexchichi-manicure) is a web-app inspired by the manicure studio I visit regularly. The web-app is built with Flask and a PostrgeSQL database, hosted on Heroku. The main goal is to reduce human error when poking around customer information in huge bunders, and save time.

functions:
- log in: the manicure studio only has 1 admin, please try logging in by username: `username`, password: `password`.
- log out: simply clears the session.
- transaction: when the cusomter completes a manicure session (or any other treatment), the admin goes to `/transaction` and record the information about it.
- top up: the studio allows regular customers to top-up their account in advance. When they come for a treatment, they do not have to pay cash, since the amount gets deducted from the stored value.
- user: a customer can get their personal information and past transactions from `/user`.
- register: a new customer should always register for a account first before accessing any of the service mentioned above.