
from webScraper import webScraper

# This class is supposed to connect the webscraping program
# and the database
class Connection:
    #ws --> webScraper , db --> database
    #TODO
    def __init__(self, db, ws:webScraper):
        self.db = db
        self.ws = ws

    #Connects and sends data to the database
    #TODO
    def dataToDB(self):
        return

    #Gets data from db
    #TODO
    def getData(self):
        return

