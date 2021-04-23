# The webscraper that gets the information from the web
import datetime
class webScraper:
    #TODO
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # Gets new listings of houses from current date
    #TODO
    def getData(self):
        #TODO endre datoopsettet så det matcher finn sitt
        date = datetime.datetime.now().strftime("%d %m %Y")
        return

    #Function that makes sure that the listing has the right date
    #TODO
    def rightDate(self)-> bool:
        return

    #Function that connects the webscraper to the right webpage
    #TODO
    def connectWeb(self):
        return


