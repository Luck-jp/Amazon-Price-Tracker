# 🛒 Amazon Price Tracker (Manual Version)

A simple Python project that tracks the price of an Amazon product and sends an email alert when the price drops below a target value.

This version is **manual (run-based)** and designed for learning web scraping and automation basics.

---

## 🚀 Features

- Scrapes product price from Amazon  
- Handles split price format (whole + fraction)  
- Cleans price formatting (removes commas)  
- Sends email alerts when price drops  
- Beginner-friendly structure  

---

## 🧰 Tech Stack

- Python 3  
- requests  
- BeautifulSoup (html.parser)  
- smtplib (built-in)  

---

## 📦 Installation

Clone the repository:

git clone https://github.com/your-username/amazon-price-tracker.git  
cd amazon-price-tracker  

Install dependencies:

pip install -r requirements.txt  

---

## ⚙️ Setup

Add your product URL in `main.py`:

URL = "YOUR_AMAZON_PRODUCT_LINK"

---

Add headers (required for Amazon scraping):

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

---

Configure email (required for alerts):

my_email = "your_email@gmail.com"  
password = "your_app_password"  

⚠️ This project sends email alerts, so you will need:
- A valid email account  
- An **App Password** (not your normal password)  

For Gmail:
- Enable 2-Step Verification  
- Generate an App Password from your Google Account  

---

## ▶️ Usage

Run the script manually:

python main.py  

If the price is below your target, you will receive an email alert.

---

## 🧠 How It Works

1. Sends request to Amazon product page  
2. Parses HTML using BeautifulSoup (html.parser)  
3. Extracts:
   - a-price-whole  
   - a-price-fraction  
4. Cleans price (removes commas)  
5. Converts to float  
6. Compares with target price  
7. Sends email if condition is met  

---

## ⚠️ Limitations

- Amazon may block requests  
- HTML structure may change  
- Script must be run manually  
- Not suitable for large-scale tracking  

---

## 🔮 Future Improvements

- Automate execution (scheduler / cron job)  
- Track price history  
- Build web interface  
- Add Telegram / WhatsApp alerts  
- Support multiple products  

---

## 📁 Project Structure

amazon-price-tracker/  
│  
├── main.py  
├── requirements.txt  
└── README.md  

---

👨‍💻 Author

Lakshay
## 📜 License

This project is for educational purposes only.

---

