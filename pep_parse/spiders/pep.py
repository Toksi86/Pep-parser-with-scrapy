import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://' + domain + '/' for domain in allowed_domains]

    def parse(self, response):
        peps = response.css('tbody')
        for pep in peps.css('a[href^="pep"]'):
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response, ):
        data = {
            'number': response.css(
                'h1.page-title::text').get().split(' ')[1],
            'name': response.css(
                'h1.page-title::text').get().split('– ')[-1],
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get()
        }
        yield PepParseItem(data)
