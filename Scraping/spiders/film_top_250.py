import scrapy
from ..items import FilmITems
from scrapy.spiders import CrawlSpider

class film_top_250(scrapy.Spider):
    name = "film_top_250"
    allowed_domains = ["www.imdb.com"]
    start_urls = [
        'https://www.imdb.com/chart/top'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'Scraping.pipelines.FilmScrapingPipeline': 300
        }
    }

    def parse(self, response):
        for result in response.css('tbody>tr>td.titleColumn>a'):
            yield scrapy.Request(url="https://www.imdb.com" + result.xpath('@href').extract_first(),callback=self.parse_detail)
    
    def parse_detail(self, response):

        items = FilmITems()

        title = response.css('h1:first-child::text').get()

        title_original = response.css('div.sc-dae4a1bc-0::text').get()
        if title_original == None:
            title_original = title
        else:
            title_original = title_original[16:]

        score = response.css('div.sc-7ab21ed2-2>span:first-child::text').get()
        genre = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]/a/span/text()').getall()
        date = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/span/text()').get()

        # Conversion durée
        duree = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]/text()').getall()
        if len(duree) == 5:
            heure = int(duree[0]) * 60
            minute = int(duree[3])
            duree = heure + minute
        elif len(duree) == 2:
            if duree[1] == "m":
                duree = int(duree[0])
            else:
                duree = int(duree[0]) * 60
        ### 

        description = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[1]/text()').get()
        acteurs = response.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div/div/div/a/text()').getall()
        public = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/span/text()').get()
        pays = response.xpath("/html/body/div[2]/main/div/section[1]/div/section/div/div[1]/section[@class='ipc-page-section ipc-page-section--base celwidget']/div[@class='sc-f65f65be-0 ktSkVi']/ul[@class='ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li[@class='ipc-metadata-list__item'][1]/div[@class='ipc-metadata-list-item__content-container']/ul[@class='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base']/li[@class='ipc-inline-list__item']/a[@class='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link']/text()").get()
        
        img_url = response.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div/div[1]/div/div[1]/img/@src').get()
        imdb_url = response.url

        items['title'] = title
        items["title_original"] = title_original
        items["score"] = float(score)
        items["genre"] = genre
        items["date"] = date
        items["duree"] = duree
        items["description"] = description
        items["acteurs"] = acteurs
        items["public"] = public
        items['pays'] = pays
        items['img_url'] = img_url
        items['imdb_url'] = imdb_url

        yield items