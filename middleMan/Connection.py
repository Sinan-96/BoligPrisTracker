from webScraper import webScraper
from database.dataBaseFunctions import *

# This class is supposed to connect the webscraping program
# and the database
class Connection:
    #ws --> webScraper , db --> database
    #TODO
    def __init__(self,ws:webScraper):
        self.ws = ws


    #Connects and sends data to the database
    #TODO
    def dataToDB(self,type,data):
        # uses a dict as a switch statement
        return {
            "addBolig": addBolig(*data),
            "addBy": addBy(*data),
            "addGate": addGate(*data),
            "addBydel": addBydel(*data),
            "updateGJpris": updateGjPris(*data)
        }.get(type)


    #Gets data from db
    #TODO
    def getData(self,type):
        return

