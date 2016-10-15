from flask import Flask
from flask import request

from dataretriever import DataRetriever

retriever = DataRetriever("GOOG")


app = Flask("__name__")

@app.route('/')
def index():
    return retriever.get_name()

@app.route('/alexa/company-year-annualized/<string:company>/<int:year>', methods=['GET'])
def getCompanyRiskYearly(company, year):
    # Look up company name to get short version
    return DataRetriever(company).get_annualized_risk_by_year(year)

@app.route('/alexa/company/<string:company>/', methods=['GET'])
def getCompany(company, year):
    # Look up company name to get short version
    return "" #DataRetriever(company) #.get_annualized_risk_by_year(year)

#@app.route('/alexa/', methods=['GET'])
#def getCompany...(company, year):
#    # Look up company name to get short version
#    return DataRetriever(company).get_annualized_risk_by_year(year)


@app.route('/vartest', methods=['GET'])
def getVarsTest():
    return "" #request..get('var', 'Default')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


#(retriever.get_annualized_risk_by_year(1)
