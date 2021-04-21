
from webScraper import webScraper

# This class is supposed to connect the webscraping program
# and the database
class Connection:
    #ws --> webScraper , db --> database
    def __init__(self, db, ws:webScraper):
        self.db = db
        self.ws = ws
