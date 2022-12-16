# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class FilmITems(scrapy.Item):
    title = scrapy.Field()
    title_original = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    date = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    public = scrapy.Field()
    pays = scrapy.Field()
    img_url = scrapy.Field()
    imdb_url = scrapy.Field()

class SerieITems(scrapy.Item):
    title = scrapy.Field()
    title_original = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    date = scrapy.Field()
    duree = scrapy.Field()
    description = scrapy.Field()
    acteurs = scrapy.Field()
    public = scrapy.Field()
    pays = scrapy.Field()
    nb_episode = scrapy.Field()
    nb_saison = scrapy.Field()
    img_url = scrapy.Field()
    imdb_url = scrapy.Field()
