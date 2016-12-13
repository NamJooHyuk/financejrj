#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_jrjDB = client[settings['MONGODB_DB']]
collect_jrj_161212 = News_jrjDB[settings['MONGODB_COLLECTION']]