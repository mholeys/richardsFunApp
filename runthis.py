from dataretriever import DataRetriever

retriever = DataRetriever("GOOG")
print(retriever.get_name())
print(retriever.get_annualized_risk_by_year(1))
