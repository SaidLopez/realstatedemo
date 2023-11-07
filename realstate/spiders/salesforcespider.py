import scrapy


class SalesforcespiderSpider(scrapy.Spider):
    name = "salesforcespider"
    #allowed_domains = ["s"]
    start_urls = ["https://trailhead.salesforce.com/en/content/learn/trails/get-started-with-product-designer"]

    def parse(self, response):
        links = response.css('.slds-grow.slds-m-vertical_small.slds-m-right_large')
        for link in links:
            yield{
                'url':link.css('a::attr(href)').get()
            }