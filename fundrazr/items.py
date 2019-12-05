# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundrazrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    campaignTitle = scrapy.Field()
    amountRaised = scrapy.Field()
    currencyType = scrapy.Field()
    percent_complete = scrapy.Field()
    goal = scrapy.Field()
    numberContributors = scrapy.Field()
    updates = scrapy.Field()
    activities = scrapy.Field()
    timeLeft = scrapy.Field()
    period = scrapy.Field()
    mediaCount = scrapy.Field()
