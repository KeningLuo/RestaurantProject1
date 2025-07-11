# Week 1: Introduction to APIs & Setup
# Tasks:
# ●	Learn API basics: keys, authentication, request/response.
#
# ●	Set up a Python environment (with requests, pandas, and json).
#
# ●	Register for API keys from:
#
# ○	Google Places
#
# ○	Yelp Fusion
#
# ○	Foursquare
#
# Milestone:
# ●	API keys obtained and successful test call made to one API.


import requests
import pandas
import json

def test_google_places(api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': 'restaurants in New York',
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data['results'][0])  # Print info of first restaurant

# Replace with your actual API key
test_google_places("AIzaSyA7Tu0WvLEhi82RRGOaeti86QL5V8CVZiU")
# succeed in Google


def test_yelp(api_key):
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    params = {
        "term": "restaurants",
        "location": "New York",
        "limit": 1
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(data['businesses'][0])  # Print first restaurant

# Replace with your actual Yelp API key
test_yelp("Txk6TFuWq1kMZGgBFTMLYUC11wWSyfp5mNwonT016ObyRrxmSxrrwzIjykZ6C2Ncwb8gn2PlWLTHi8O-hmdZtgVAYNl_H2Gc4XJbY1b4MbVkn9X8pp2UOiEjzAtuaHYx")
# succeed in Yelp


def test_foursquare(api_key):
    url = "https://places-api.foursquare.com/places/search"
    headers = {
        "Accept": "application/json",
        "Authorization": api_key,
        "X-Places-Api-Version": "2025-06-17"
    }
    params = {
        "query": "restaurant",
        "near": "New York, NY",
        "limit": 1
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(json.dumps(data, indent=2)) # print the message or result

    if 'results' in data and data['results']:
        print("\nFirst restaurant:")
        print(json.dumps(data['results'][0], indent=2)) # print the first restaurant
    else:
        print("\nNo results found or 'results' key missing.")

# Replace this with the FULL key starting with fsq3...
test_foursquare("fsq33x2GQQ6fBK79kRuQvMYdE3yRfJPSMJr6j9B1vww8I2M=")
# failed in Foursquare
# having troubles with version and token
# Service key: SLD0YJ3FBSOQGEDVTWD3FOXZJONCOJLPZSUQQLL155AT1RLA
# legacy key: fsq33x2GQQ6fBK79kRuQvMYdE3yRfJPSMJr6j9B1vww8I2M=
