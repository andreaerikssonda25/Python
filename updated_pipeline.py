#Extracted and transformed data from json to .csv

import requests
import json
import pandas as pd

#Pull data from Spoonacular API from the free APIs list given
#List the recipes from Greece

api_key = "e62f42c18d824361badd2c48e3811a58"

main_url = "https://api.spoonacular.com"

#Define the parameters of the query and build the request (Greek recipes)
query_params = {'apiKey': api_key, 'cuisine': 'greek', 'number':30}
response = requests.get(f'{main_url}/recipes/complexSearch', params=query_params)
json = response.json()


#Put them in ascending order by recipe title
title_order = sorted(json["results"], key=lambda x : x['title'])
#Use lambda (anonymous function) to sort through the dictionary by title
#Sort specifically by the results portion listed above


df=pd.DataFrame(title_order)
df

#List the calorie count per recipe
#Build the query params

query_params = {'apiKey': api_key}
#r is each curly brace set

calories = []

for r in title_order:
    route = f'{main_url}/recipes/{r["id"]}/nutritionWidget.json'
    response = requests.get(route, params=query_params)
    json = response.json()
    calories.append(json["calories"])
    
df["calories"] = calories

df.head()

df.to_csv("greek recipe calories.csv")
#load to new .csv