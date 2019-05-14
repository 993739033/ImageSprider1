from scrapy.cmdline import execute


if __name__=="__main__":
    # execute("scrapy crawl ImgSprider".split( ))
    execute(["scrapy","crawl","ImgSprider"])