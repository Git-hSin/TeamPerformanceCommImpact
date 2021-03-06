import requests
import json
import zillow
import pandas as pd
import pprint
from config import zkey

key = zkey

api = zillow.ValuationApi()

address = "1801 Meridian Avenue, South Pasadena, CA"
postal_code = "91030"

data = api.GetSearchResults(key, address, postal_code)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data.get_dict())