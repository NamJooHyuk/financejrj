#encoding:utf-8
import scrapy
import re
from scrapy.selector import Selector
from financejrj.items import FinancejrjItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule

class ExampleSpider(CrawlSpider):
    name = "jrjnews"
    allowed_domains = ["jrj.com.cn"]
    start_urls = ['http://www.jrj.com.cn/']
    rules=(
        Rule(LinkExtractor(allow="([\w]+)\.jrj\.com\.cn/2016/12/12([\w\.]+)"),
        callback="parse_news",follow=True),
    )
    def printcn(suni):
        for i in uni:
            print uni.encode('utf-8')
    def parse_news(self,response):
        item = FinancejrjItem()
        item['news_thread']=response.url.strip().split('/')[-1][:-6]
        # self.get_thread(response,item)
        self.get_title(response,item)
        self.get_time(response,item)
        self.get_url(response,item)
        self.get_news_from(response,item)
        self.get_from_url(response,item)
        self.get_text(response,item)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!remenber to Retrun Item after parse
        return item 
    def get_title(self,response,item):
        title=response.xpath("/html/head/title/text()").extract()
        if title:
            # print 'title:'+title[0][:-5].encode('utf-8')
            item['news_title']=title[0][:-9]

    def get_time(self,response,item):
        time=response.xpath("/html/body/div[1]/div[3]/div[1]/div[3]/p/span[1]/text()").extract()
        if time:
            # print 'time'+time[0][:-5].encode('utf-8')
            item['news_time']=time[0]

    def get_news_from(self,response,item):
        news_from=response.xpath("/html/body/div[1]/div[3]/div[1]/div[3]/p/span[2]/text() | /html/body/div[1]/div[3]/div[1]/div[3]/p/span[2]/a/text()").extract()
        if news_from:
            # print 'from'+news_from[0].encode('utf-8')     
            item['news_from']=news_from[0]

    def get_from_url(self,response,item):
        from_url=response.xpath("/html/body/div[1]/div[3]/div[1]/div[3]/p/span[2]/a/@href").extract()
        if from_url:
            # print 'url'+from_url[0].encode('utf-8')       
            item['from_url']=from_url[0]    

    def get_text(self,response,item):
        news_body=response.xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/p/text()").extract()
        if news_body:
            # for  entry in news_body:
            #   print entry.encode('utf-8')
            item['news_body']=news_body 
    def get_url(self,response,item):
        news_url=response.url
        if news_url:
            #print news_url 
            item['news_url']=news_url
