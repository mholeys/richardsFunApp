import requests
import json

"""
For the examples we are using 'requests' which is a popular minimalistic python library for making HTTP requests.
Please use 'pip install requests' to add it to your python libraries.
"""

# portfolioAnalysisRequest = requests.get("https://test3.blackrock.com/tools/hackathon/performance", params= {'identifiers':"IXN"})
# text = portfolioAnalysisRequest.text # get in text string format
# portfolioAnalysisRequest.json # get as json object

with open('somedata.json') as json_data:
    data = json.load(json_data)
    

def get_name():
    return data['requests'][0]['identifiers'][0]['identifier']

#print(get_security_id())
