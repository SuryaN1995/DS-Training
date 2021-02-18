import scrapy


class AllPageSpider(scrapy.Spider):
    name = 'all_page'
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
            nextPage = response.css('li.next > a::attr(href)').extract_first()
            if nextPage:
                nextPage = response.urljoin(nextPage)
                yield scrapy.Request(url=nextPage,callback=self.parse)
