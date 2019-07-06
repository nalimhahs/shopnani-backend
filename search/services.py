import os
import requests

# The function accepts a query and passes it to the flipkart api. 
# The results are then converted to json and then returned.
# The affiliate ID and Token are stored as environment variables to prevent unintentional exposure. 

def getResultsService(query):
  affiliateId = os.environ.get('DJANGO_FK_AFFILIATE_ID')
  affiliateToken = os.environ.get('DJANGO_FK_AFFILIATE_TOKEN')
  url = 'https://affiliate-api.flipkart.net/affiliate/1.0/search.json'
  headers = {"Fk-Affiliate-Id": affiliateId,
              "Fk-Affiliate-Token": affiliateToken}
  params = {'query': query, 'resultCount': 10}
  r = requests.get(url=url, headers=headers, params=params)
  results = r.json()
  return results
