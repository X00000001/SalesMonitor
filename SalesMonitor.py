import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os

# ====== CONFIGURATION ======
WISHLIST_URL = #"WEBSITE TO MONITOR"
STORED_LIST_FILE = #"WHERE DO YOU WANT TO SAVE YOUR LIST?"   
EMAIL_FROM = #"FROM EMAIL"     
EMAIL_TO = #"TO EMAIL"       
APP_PASSWORD = #"YOUR GOOGLE GMAIL APP PASSWORD"      
# ============================

#This next class will find the class you're looking to parse, and tabulate them into the .txt document.

def fetch_current_knives():
    response = requests.get(WISHLIST_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    knives = []

    for product in soup.find_all('li', class_='product'):
        # Get Knife Name
        title_tag = product.find('h3', class_='card-title')
        name = title_tag.find('a').text.strip() if title_tag else "Unnamed Knife"

        # Get Stock Status
        stock_tag = product.find('p', class_='instock-text')
        stock_status = stock_tag.text.strip().upper() if stock_tag else "Out of Stock"

        knives.append(f"{name} || {stock_status}")

    return sorted(knives)



def load_previous_knives():
    if not os.path.exists(STORED_LIST_FILE):
        return []
    with open(STORED_LIST_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]



def save_current_knives(knives):
    with open(STORED_LIST_FILE, 'w') as file:
        for knife in knives:
            file.write(f"{knife}\n")

#This is where the program will create the email to send to the user

def send_email_notification(sold_items):
    subject = "🔪 Knife Sold Alert!"
    body = f"The following knife(knives) have been sold:\n\n" + "\n".join(sold_items)  #you can change this message to say whatever you want
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_FROM, APP_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())


#This will do your diff between old and new

def main():
    current_knives = fetch_current_knives()
    previous_knives = load_previous_knives()

    if not previous_knives:
        save_current_knives(current_knives)
        print("Initial knife list saved. Monitoring started.") #this is just a message telling you what's going on with the program
        return

    sold_items = [knife for knife in previous_knives if knife not in current_knives]

    if sold_items:
        send_email_notification(sold_items)
        print(f"Alert sent! Sold knives: {sold_items}")  #if something sells, it'll tell you here
        save_current_knives(current_knives)
    else:
        print("No changes detected.")  #assuming that nothing sells, you'll get this



import time  #you need to be able to count time here

if __name__ == "__main__":
    print("KnifeMonitor started. Monitoring every 15 minutes...")  #This keeps the program running provided your terminal is open
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error occurred: {e}")
        time.sleep(900)  # 900 seconds = 15 minutes

