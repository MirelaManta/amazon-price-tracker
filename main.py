import requests
from bs4 import BeautifulSoup
from dotenv.main import load_dotenv
import os
import smtplib

load_dotenv()
my_email = os.environ["MY_EMAIL"]
password = os.environ["MY_PASSWORD"]
URL = "https://www.amazon.com/COSORI-Airfryer-Dishwasher-Safe-freidora-Exclusive/dp/B0936FGLQS/ref=sr_1_2_sspa?crid=3QU2DDJ38E353&keywords=air%2Bfryer&qid=1680959373&sprefix=air%2Bfrayer%2Caps%2C430&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzT00xVjBURUo1VkRKJmVuY3J5cHRlZElkPUEwNjc1NzA4MlFENEdYQkFaWjY1NSZlbmNyeXB0ZWRBZElkPUEwMzc0MTkwVzRCT0lFUUZIQzhQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Accept-Language": "en,en-US;q=0.5"
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price_with_currency = soup.find(name="span", class_="a-offscreen").getText()
price = float(price_with_currency.strip("$"))
product_title = soup.find(name="span", id="productTitle").getText().strip()

WISHED_PRICE = 89
if price < WISHED_PRICE:
    message = f"{product_title} is now ${WISHED_PRICE}."
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{URL}".encode("utf-8")
        )
