from . import session


class Vehicle(object):
    def __init__(self, vin, year=None):
        self.vin = vin
        self.year = year
        self.listing = {}
        self.message = None

    def decode(self):
        path = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{}?format=json"
        if self.year is not None:
            path += "&modelyear={}".format(self.year)
        path = path.format(self.vin)
        response = session.get(path).json()
        for i in response['Results']:
            self.listing[i['Variable']] = i['Value']
        self.message = response['Message']
