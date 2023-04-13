# Amazon Price Tracker

As a dedicated online shopper, I often find myself browsing different websites for products I want to buy. However, I don't always want to pay full price for these items. That's why I created this Amazon Price Tracker.

This Python script uses the __requests__ and __beautifulsoup4__ libraries to scrape the Amazon website for information about a specific(here, a COSORI Air Fryer) product. It then checks the current price of the product against a desired price set by the user.

If the current price of the product falls below the desired price, the script sends an email notification to the user. The email includes a link to the product on Amazon and a message notifying the user that the price has dropped.
## Installation
To use this script, you'll need to have Python 3 installed on your machine, as well as the requests, beautifulsoup4, and python-dotenv libraries. You can install these libraries using pip:
```
pip install requests beautifulsoup4 python-dotenv
```
You'll also need to create a .env file in the same directory as the script. This file should contain your email address and password for a Gmail account. For security reasons, I recommend creating a new Gmail account specifically for this project.
```
MY_EMAIL=your_email_address
MY_PASSWORD=your_email_password
```
## Usage
To use the script, simply run it from the terminal:
```
python filename.py
```
You can customize the product you want to track as well as the desired price. The script will then scrape the website and send an email notification if the price drops below the desired price.
## License
This project is licensed under the __MIT License__ - see the LICENSE file for details.
