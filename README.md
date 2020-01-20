# Web scrapping and analysing
Fundrazr data collection, mining and analysis.

# Overview
This project aim towards collecting data from https://fundrazr.com/ for category animals and using the data to analyse whether a particular campaign is going to reach its goal or not.

# Steps for scraping data using python's scrapy
1. Make a folder called Web-scrapping-and-analysing. Using terminal run command "scrapy startproject fundrazr" inside the folder to create scrapy project.
2. Define all the fields you want to scrape in items.py.
3. Main code for the program is in /fundrazr/spiders/fundrazr_scrape.py.
4. Code is scraping required fields from the website using xpath obtained after inspecting the page.
5. Same piece of code is repeated to loop through each page and get data of each and every campaign.
6. To excecute code run the command "scrapy crawl fundrazr_scraper -o data.csv".
7. Data obtained by scraping is stored in data.csv.

# Analysing scraped data
1. Preprocessing
  a. Covert numerical data into integers using regular expressions.
  b. Remove redundant data like "campaign title" data.
  c. Create dependent variable with use of "percent_complete" column. If percent_complete by the campaign is 100% or more, y variable will      be 1 or else it'll be 0.
  d. Divide the data in training set and test data and scale it.
2. Model testing
  a. Amongst logistic regression, KNN, SVM, naive bayes, random forest and xgboost; xgboost has performed best with accuracy of --------------------------.
