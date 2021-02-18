import scrapy


class FullPageSpider(scrapy.Spider):
    name = 'full_page'
    allowed_domains = ['toscrape.com/']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        cellList = response.css('div.quote')
        for cell in cellList:
            yield {
                'author' : cell.css('small.author::text').extract_first(),
                'text' : cell.css('span.text::text').extract_first(),
                'tags' : cell.css('a.tag::text').extract(),
            }
