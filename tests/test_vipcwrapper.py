from vpicwrapper import pyvpic


def test_vin_info():
    vehicleinstance = pyvpic.Vehicle('5UXWX7C5*BA')
    vehicleinstance.decode()
    assert isinstance(vehicleinstance.listing, dict)
