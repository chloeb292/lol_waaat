
# Flask imports
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON/API Request Imports for PandaScore
import requests
import json
from operator import itemgetter
import readline


_TOKEN = "2VFXG97HWPjCekpX7HpLMCAZQgr15N2NN5spSg89bGBw2s4vG1Q"

### WEB APP 

@app.route('/')
def index():
    return "Link to <a href='/leagues'>Leagues</a>"

@app.route("/leagues")
def leagues(): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    ll = get_leagues()
    #return "Check console for list of leagues"
    return render_template("leagues.html", message="This is the list of League of Legend Leagues!", leagues = ll, route_rule= route_rule );   

@app.route("/series/<league_id>")
def series(league_id): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    series = get_series(league_id)
    #return "Check console for list of leagues"
    return render_template("series.html", message="ZOMG MY DAD IS SO SMART!", series = series, route_rule= route_rule ); 

@app.route("/tournaments/<serie_id>")
def tournaments(serie_id): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    tournaments = get_tournaments(serie_id)
    return render_template("tournaments.html", message="These are the tournaments for the series", tournaments = tournaments, route_rule= route_rule );   


@app.route("/matches/<tournament_id>")
def matches(tournament_id): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    matches = get_matches(tournament_id)
    return render_template("matches.html", message="These are the matches for the tournaments", matches = matches, route_rule= route_rule );

@app.route("/opponents/<match_id>")
def opponents(match_id): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    opponents = get_opponents(match_id)
    return render_template("opponents.html", message="These are the opponents for this match", opponents = opponents, route_rule= route_rule );   

@app.route("/players/<team_id>")
def players(team_id): 
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    players = get_players(team_id)
    bread = get_bread(team_id)
    return render_template("players.html", message="These are the players on this team", players = players, bread= bread );

@app.route("/team")
def team(): 
    team_id = request.args['team_id']
    match_id = request.args['match_id']
    route_rule = request.url_rule
    print("Current route rule -> %s <-- " % route_rule)
    players = get_players(team_id)
    bread = get_bread(team_id)
    return render_template("players.html", message="These are the players on this team", players = players, bread= bread );



# functional library
#funcitons for PandaScore requests: 
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


# lookup a single series from the serie 
# TAKE PARAM FOR LEAGUE_ID
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

def get_players(team_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[team_id]=%s" % team_id
    og_url = ("https://api.pandascore.co/lol/players")
    url = og_url + token + params
    print(url)
    # Make a normal HTTP request to the endpoint, getting a response object
    response = requests.get(url)
    # we're going to UTF-8 decode the byte array into a normal string. 
    raw_json = response.content.decode('utf-8') 
    json_object = json.loads(raw_json)
    return json.loads(raw_json)

def get_bread(team_id):
    token = "?token=%s" % _TOKEN
    params= "&filter[opponent_id]=%s" % team_id
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





    <ul class="breadcrumb">
        <li><a href="/leagues">Leagues</a> </li>
        <li> <a href="/series/{{ bread[0]['league_id']}}">  Series </a> </li>
        <li> <a href="/tournaments/{{bread[0]['serie_id']}}">  Tournaments </a> </li>
        <li> <a href="/matches/{{bread[0]['tournament_id']}}">  Matches </a></li>
        <li> <a href="/opponents/{{bread[0]['id']}}">  Opponents </a> </li>
        <Li> Players</Li>
    </ul>

