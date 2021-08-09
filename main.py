import scrapy
from scrapy.crawler import CrawlerProcess


class QoutesScraper(scrapy.Spider):
    name = "Qoutes"
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response, **kwargs):
        for _qoute in response.css(".quote"):
            yield {
                "Text": _qoute.css(".text::text").get(),
                "Author": _qoute.css(".author::text").get(),
                "Tags": _qoute.css(".tag::text").getall()
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


process = CrawlerProcess()
process.crawl(QoutesScraper)
process.start()
