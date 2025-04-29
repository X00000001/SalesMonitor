SalesMonitor


A little tool to monitor whether something, in this case some collectible pocket knives, have sold on a website.  I use this to monitor consignment pieces that I've sent to various retailers, so that I know when one of the knives has sold.  Using a public Wishlist feature on a website, I'm able to take the knives and put them into a list which exposes a public URL that allows me to scrape the website for In/Out of stock listings.  I'm running this Python script on my Mac every 15 minutes to look at snapshots and write a small Txt file back to my computer.  When it detects a change in the website, it'll use an app key from a Gmail account to send an email to myself, denoting the difference it detected.  

Originally built for personal use, it's ideal for collectors and enthusiasts who don't want to miss a blade going off the market.

You can either use this to monitor a Wishlist like I have, which allows you to determine if a consignment piece has sold, OR... if you're really clever, you can use it to monitor a New Products page and get a digest of what's new that's come in... or use it to see if a product that's out of stock is back in stock by pointing it at a specific product page... be creative about it.  

Heck, this framework with a few modifications could easily be used to monitor any kind of webpage and detect a change.  If you wanted to you could change a few classes and use it to monitor a forum to see if someone in particular has posted something, or point it at a deal aggregator site to see when something goes on sale, or point it to a particular eBay search query to see if a particular item comes up for sale... the possibilities are endless.  

FEATURES

- ✅ Scrapes wishlist page HTML using `BeautifulSoup`
- ✅ Detects stock changes (e.g., "In Stock" → "Out of Stock")
- ✅ Sends email alerts with knife name and link
- ✅ Persists previous state to avoid duplicate notifications
- ✅ Works with `cron` or as a continuously running service



REQS


- Python 3.7+
- `beautifulsoup4`
- `requests`
- A Gmail account (with [App Passwords](https://support.google.com/accounts/answer/185833))


CLONE THIS REPO:
git clone https://github.com/yourusername/knifemonitor.git
cd knifemonitor


INSTALLATION GUIDE

Obviously, you need to install Python first.  If you haven't... well, you're not going to be able to use this.  Go to https://www.python.org/downloads/ and download the latest version of Python, I'm using Python 3.13.3.  From there, make sure you have Pip, Python's package manager, since we're going to need it to download and install Beautifulsoup.  


Now you need to change a few variables.  
FROM_EMAIL = "youraddress@gmail.com"
TO_EMAIL = "youraddress@gmail.com"
APP_PASSWORD = "your-gmail-app-password"

You will also need to set the specific URL that you're monitoring.  

Change your from and to emails to be the email address you want the email to come from and go to.  If you're working as a sales consultant, you can actually set this up to automate some work for you.  Build a list of a customer's products, and then automatically notify them via email when one sells.  Pretty nifty, eh?  You can even add multiple fields if you want to send an email to a customer and yourself, maybe if you need to automate another process like queuing up a payout to them.  


RUNNING IN THE BACKGROUND

I've set this program up to be able to run continuously in the background, although you'll need to keep your terminal open during the process.  I guess I could have coded it so it'd register as a service on a Mac and run in the bg, but that was too much work.  If you want to do that, feel free to modify the code and submit a PR.  The program will run every 15 minutes and check the website you've specified, and determine any diffs.  If at any point you want to see the list that it's exporting for some reason... there'll be a .txt file that the program spits out into the folder you installed the program that it keeps up to date.  
