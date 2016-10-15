import requests
import json

class DataRetriever:

    def __init__(self, comp):
        portfolioAnalysisRequest = requests.get("https://www.blackrock.com/tools/json/performance", params= {'identifiers':comp})
        text = portfolioAnalysisRequest.text # get in text string format
        self.data = json.loads(text)
        self.name = comp

    def get_name(self):
        return self.data['requests'][0]['identifiers'][0]['identifier']

    def get_security_id(self):
        return self.data['resultMap']['RETURNS'][0]['securityId']

    def get_annualized_risk_by_year(self, year):
        basic_loc = self.data['resultMap']['RETURNS'][0]['monthEndPerf']

        if (year == 1):
            return basic_loc['oneYearAnnualized']

        if (year == 2):
            return basic_loc['twoYearAnnualized']
