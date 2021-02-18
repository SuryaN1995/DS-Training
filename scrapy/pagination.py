import scrapy


class PaginationSpider(scrapy.Spider):
    name = 'pagination'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for cell in response.css('div.quote'):
            item = {
                'author' : cell.css('small.author::text').extract_first(),
                'text' : cell.css('span.text::text').extract_first(),
                'tags' : cell.css('a.tag::text').extract(),
            }
            yield item
