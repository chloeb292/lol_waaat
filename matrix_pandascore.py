# Flask imports
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON/API Request Imports for PandaScore
import requests
import json
from operator import itemgetter
import readline
import urllib
import urllib.parse as urlparse
from urllib.parse import parse_qs


_TOKEN = "2VFXG97HWPjCekpX7HpLMCAZQgr15N2NN5spSg89bGBw2s4vG1Q"



# lookup a single series from the serie 
# TAKE PARAM FOR LEAGUE_ID

def get_leagues():
    token = "?token=%s" % _TOKEN
    og_url = ("https://api.pandascore.co/lol/leagues")
    url = og_url + token
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)


def get_series(league_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[league_id]=%s" % league_id
    og_url = ("https://api.pandascore.co/lol/series")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)


def get_tournaments(serie_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[serie_id]=%s" % serie_id
    og_url = ("https://api.pandascore.co/lol/tournaments")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)

def get_matches(tournament_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[tournament_id]=%s" % tournament_id
    params2= "&filter[detailed_stats]=true"
    og_url = ("https://api.pandascore.co/lol/matches")
    url = og_url + token + params + params2
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)



def get_opponents(match_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[id]=%s" % match_id
    og_url = ("https://api.pandascore.co/lol/matches")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)

def get_players(opponent1_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[team_id]=%s" % opponent1_id
    og_url = ("https://api.pandascore.co/lol/players")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)
def get_players(opponent2_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[team_id]=%s" % opponent2_id
    og_url = ("https://api.pandascore.co/lol/players")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)

def get_bread(opponent1_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[id]=%s" % opponent1_id
    og_url = ("https://api.pandascore.co/lol/matches")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)

# put functions to get HTTP requests here 
