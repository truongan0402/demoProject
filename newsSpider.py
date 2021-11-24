import scrapy

 
class NewsSpider(scrapy.Spider):
    name = 'spiderNews'
    start_urls = ['https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y']
    allowed_domains = 'reuters.com'
    
    def parse(self, reponse):
        for news in reponse.css('body'):
            yield{
                'title': news.css('h1.Headline-headline-2FXIq.Headline-black-OogpV.ArticleHeader-headline-NlAqj::text').get(),
                'content': news.css('p.Paragraph-paragraph-2Bgue.ArticleBody-para-TD_9x::text').getall(),     
            }
            