import requests
import smtplib
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv

load_dotenv()

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

my_email = os.getenv("my_email")
password = os.getenv("password")
URL = os.getenv("URL")

# Write your code below this line 👇

response = requests.get(URL, headers = header)
price_webpage = response.text

soup = BeautifulSoup(price_webpage, "html.parser")


price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")  

if price_whole is not None:
    whole = price_whole.getText().replace(",", "")  
    fraction = price_fraction.getText() if price_fraction else "00"
    price = whole + fraction
else:
    print("Price not found.")
final_price = float(price)

if final_price < 2500:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "XXXXXXXXXXXXXXXXXX@gmail.com",
            msg = f"Subject: Katana Price Alert\n\nThe Katana is now below Rs{final_price}!"
        )
    print("Email sent!")
