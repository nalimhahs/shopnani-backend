import os
import requests


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
