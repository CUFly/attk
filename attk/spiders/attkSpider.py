import scrapy
from scrapy import Request
from ..items import AttkItem

class AttkspiderSpider(scrapy.Spider):
    name = 'attkSpider'
    allowed_domains = ['attack.mitre.org']
    # start_urls = ['https://attack.mitre.org/']
    current_page = 1001

    def start_requests(self):
        start_url = 'https://attack.mitre.org/techniques/T1001/'
        yield Request(start_url, callback=self.parse)

    def parse(self, response):
        list_selector = response.xpath("//div[@class='card-body']")
        print(list_selector)
        try:
            # item = AttkItem()
            # Id = scrapy.Field()
            # sub_tech = scrapy.Field()
            # tactic = scrapy.Field()
            # platform = scrapy.Field()
            # data_source = scrapy.Field()
            # require_network = scrapy.Field()
            # version = scrapy.Field()
            # created_data = scrapy.Field()
            # last_modify_data = scrapy.Field()
            Id = list_selector.xpath("./div[@id='card-id']/text()").extract_first()
            name = response.xpath("//div[@class='container-fluid']/h1/text()").extract_first().strip('\n').strip()
            sub_tech = list_selector.xpath("./div[@class='card-data']/a/text()").extract()
            tactic = list_selector.xpath("./div[@id='card-tactics']/text()").extract_first().strip('\n').strip()
            # platform = list_selector.xpath("'/div[@id='card-platforms']/text()").extract_first()
            dic_item = {
                "Id": Id,
                "name": name,
                "sub_tech": sub_tech,
                "tactic": tactic,
                "url": 'https://attack.mitre.org/techniques/T%s/' % Id
            }

            yield dic_item
        except:
            pass
        while True:
            if self.current_page > 9999:
                break
            self.current_page += 1
            url = 'https://attack.mitre.org/techniques/T%d/' % self.current_page
            yield Request(url, callback=self.parse)



    def tech_parse(self, response):
        pass


