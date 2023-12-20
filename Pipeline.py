import requests
import json

#Extract data from a public API (Spoonacular). Use GET to make the request
main_url = "https://api.spoonacular.com"
#Define params, incl. my API key and narrowed down cuisine type (params defined in .ipynb)
response = requests.get(f'{main_url}/recipes/complexSearch', params=query_params)

#Transform and organize data by alphabetical order and calorie count 
title_order = sorted(json["results"], key=lambda x : x['title'])
df=pd.DataFrame(title_order)

#Add in a new df to get calorie count column (params in .ipynb)
calories = []
df["calories"] = calories

#Load
df.to_csv("greek recipe calorie counts.csv")