# Web scrapping and analysing
Fundrazr data collection, mining and analysis.

# Overview
This project aim towards collecting data from https://fundrazr.com/ for category animals and using the data to analyse whether a particular campaign is going to reach its goal or not.

# Steps for scraping data using python's scrapy
1. Make a folder called Web-scrapping-and-analysing. Using terminal run command -------------------- inside the folder to create scrapy project.
2. Define all the fields you want to scrape in items.py.
3. Main code for the program is in /fundrazr/spiders/fundrazr_scrape.py.
4. Code is scraping required fields from the website using xpath obtained after inspecting the page.
5. Same piece of code is repeated to loop through each page and get data of each and every campaign.
6. To excecute code run the command --------------------.
7. Data obtained by scraping is stored in data.csv.

# Analysing scraped data
1. Preprocessing
  a. Covert numerical data into integers using regular expressions.
  b. Remove redundant data like campaign title which is not useful analysis of data.
  c. Create dependent variable with use of 
