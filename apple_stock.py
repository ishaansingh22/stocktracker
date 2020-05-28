import requests
from bs4 import BeautifulSoup
import smtplib
import time

def checkPrice():
    r = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch')
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', {'class': "My(6px) Pos(r) smartphone_Mt(6px)"}).find('span').text
    conv_price = float(price)

    if conv_price > 320.00:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(#enter your email, #enter your email password)

    subject = 'Daily Apple Stock Tracker'
    body = 'Apple stock is high right now. Check out the market: https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        #your email from which the bot will send an email,
        #receiver's email,
        msg
    )
    print('Email has been sent')
    server.quit

while True:
    checkPrice()
    time.sleep(86400)

