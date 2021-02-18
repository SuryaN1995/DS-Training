import scrapy


class OneOnequoteSpider(scrapy.Spider):
    name = 'one_onequote'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/random']

    def parse(self, response):
        return {
            'author' : response.css('small.author::text').extract_first(),
            'text' : response.css('span.text::text').extract_first(),
            "tags" : response.css('a.tag::text').extract(),
        }
