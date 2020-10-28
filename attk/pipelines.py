# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# Id = scrapy.Field()
#     sub_tech = scrapy.Field()
#     tactic = scrapy.Field()
#     platform = scrapy.Field()
#     data_source = scrapy.Field()
#     require_network = scrapy.Field()
#     version = scrapy.Field()
#     created_data = scrapy.Field()
#     last_modify_data = scrapy.Field()

class AttkPipeline:
    def process_item(self, item, spider):
        return item

# class CSVPipeline:
#     index = 0
#     file = None
#     file_name = 'Attk.csv'
#
#     def open_spider(self, spider):
#         self.file = open(self.file_name, 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         if self.index == 0:
#             column_name = "Id, sub_tech, tactic, platform, data_source, require_network, version, created_data, last_modify_data"
#             self.file.write(column_name)
#             self.index = 1
#         temp_s = ''
#         for sub in item['sub_tech']:
#             temp_s += sub + ', '
#         item['sub_tech'] = temp_s.rstrip(', ')
#         l_str = item['Id'] + ", " + \
#                    item['sub_tech'] + ", " + \
#                    item['tactic'] + "\n"
#                    # item['platform'] + ", " + \
#                    # item['data_source'] + ", " + \
#                    # item['require_network'] + ", " + \
#                    # item['version'] + ", " + \
#                    # item['created_data'] + ", " + \
#                    # item['last_modify_data'] + '\n'
#         self.file.write(str(l_str))
#
#     def close_spider(self, spider):
#         self.file.close()
