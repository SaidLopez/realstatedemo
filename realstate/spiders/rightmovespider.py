import scrapy


class RightmovespiderSpider(scrapy.Spider):
    name = "rightmovespider"
    allowed_domains = ["rightmove.co.uk"]
    start_urls = ["https://www.rightmove.co.uk/property-for-sale/find.html?includeSSTC=false&keywords=&sortType=2&viewType=LIST&channel=BUY&index=0&radius=0.0&maxDaysSinceAdded=7&locationIdentifier=OUTCODE%5E2829&showSuggestionFeedback=true"]

    def parse(self, response):
        houses = response.css('.l-searchResults>div')

        for house in houses:
            yield {
                'price' : house.css('.propertyCard-priceValue::text').get(),
                'type' : house.css('h2.propertyCard-title::text').get(),
                'address' : house.css('meta[itemprop="streetAddress"]').attrib['content'],
                'link' : house.css('a.propertyCard-link').attrib['href'],
                'rooms' : house.css('h2.propertyCard-title::text').get(),
                
            }
            