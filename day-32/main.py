import smtplib as smtp
import datetime as dt

SMTP_SERVER = "smtp.gmail.com"
EMAIL= "automated.kamilsuwada@gmail.com"
TO = "kamilsuwada@icloud.com"
PASS = "it_works_with_right_pass ;)"



def send_email(msg: str, to_addr: str):
    connection = smtp.SMTP(SMTP_SERVER)
    connection.starttls()
    connection.login(user=EMAIL, password=PASS)
    connection.sendmail(from_addr=EMAIL, to_addrs=to_addr, msg=msg)
    connection.close()


now = dt.datetime.now()
year = now.year
month = now.year
day = now.day
week_day = now.weekday()


dob = dt.datetime(year=1996, month=1, day=2, hour=19, minute=30)