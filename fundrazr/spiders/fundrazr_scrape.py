import scrapy
from fundrazr.items import FundrazrItem
from datetime import datetime
import re


class Fundrazr(scrapy.Spider):
	name = "fundrazr_scraper"

	# First Start Url
	start_urls = ["https://fundrazr.com/find?category=Animals"]

	npages = 1211

	# This mimics getting the pages using the next button. 
	for i in range(1, npages):
		start_urls.append("https://fundrazr.com/find?category=Animals&page="+str(i)+"")

	def parse(self, response):
		for href in response.xpath("//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"):
			# add the scheme, eg http://
			url  = "https:" + href.extract()
			yield scrapy.Request(url, callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = FundrazrItem()

		# Getting Campaign Title
		item['campaignTitle'] = response.xpath("//*[@id='campaign-title']/text()").extract()[0].strip()

		# Getting Amount Raised
		item['amountRaised']= response.xpath("//*[@id='campaign-stats']/div[1]/span[1]/span[2]/text()").extract()

		# Currency Type (US Dollar Etc)
		item['currencyType'] = response.xpath("//*[@id='campaign-stats']/div[1]/@title").extract()

		# Goal
		item['percent_complete'] = response.xpath("//*[@id='campaign-stats']/div[1]/span[3]/span/text()").extract()

		# Goal
		item['goal'] = response.xpath("//*[@id='campaign-stats']/div[1]/span[3]/text()").extract()[1].strip()

		# Number of contributors
		item['numberContributors'] = response.xpath("//*[@id='campaign-stats']/div[2]/span[1]/text()").extract()

		# Number of updates
		item['updates'] = response.xpath("//*[@id='feed-nav']/li[2]/a/span/text()").extract()

		# Number of activities posted
		item['activities'] = response.xpath("//*[@id='feed-nav']/li[3]/a/span/text()").extract()

		# Time left
		item['timeLeft'] = response.xpath("//*[@id='campaign-stats']/div[3]/span/span[1]/text()").extract()

		# Days or weeks or year
		item['period'] = response.xpath("//*[@id='campaign-stats']/div[3]/span/span[2]/text()").extract()

		# Media count
		item['mediaCount'] = response.xpath("//*[@id='video-link']/a[2]/span/span/text()").extract()

		yield item
