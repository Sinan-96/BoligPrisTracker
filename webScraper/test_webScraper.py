import unittest
from datetime import datetime
from webScraper.webScraper import webScraper


class testWebScraper(unittest.TestCase):
    # Tests that the data that is extracted is correct
    def test_getBoligData(self):
        ws = webScraper()
        self.assertEqual(ws.getBoligData("https://www.finn.no/realestate/homes/ad.html?finnkode=216548832")
                         ,{75,99,datetime.now().date(),'Oslo','Majorstuen','Harald Hårfagres gate'})
        self.assertEqual(ws.getBoligData("https://www.finn.no/realestate/homes/ad.html?finnkode=216564331")
                         , {23, 48, datetime.now().date(), 'Oslo', 'Vestli', 'Ragnhild Schibbyes vei'})

    #Test if it the function enters all the new listings as it should
    #TODO
    def test_traverseNew(self):
        return



