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

import matrix_pandascore as ps 


### WEB APP 

@app.route('/')
def index():
    return "Link to <a href='/leagues'>Leagues</a>"

@app.route("/leagues")
def leagues(): 
    
    ll = ps.get_leagues()
    #return "Check console for list of leagues"
    return render_template("leagues.html", message="This is the list of League of Legend Leagues!", leagues = ll);   

@app.route("/series")
def series(): 
    league_id = request.args["league_id"]
    series = ps.get_series(league_id)
    #return "Check console for list of leagues"
    return render_template("series.html", series = series); 

@app.route("/tournaments")
def tournaments(): 
    serie_id = request.args["serie_id"]
    tournaments = ps.get_tournaments(serie_id)
    return render_template("tournaments.html", message="These are the tournaments for the series", tournaments = tournaments);   


@app.route("/matches")
def matches(): 
    tournament_id = request.args["tournament_id"]
    matches = ps.get_matches(tournament_id)
    return render_template("matches.html", message="These are the matches for the tournaments", matches = matches);


@app.route("/opponents")
def players(): 
    match_id = request.args["match_id"]
    opponent1_id = request.args["opponent1_id"]
    opponent2_id = request.args["opponent2_id"]
    match = ps.get_opponents(match_id)
    team1 = ps.get_players(opponent1_id)
    team2 = ps.get_players(opponent2_id)
    return render_template("opponents.html", message="this is the info on the match", match = match, team1= team1, team2 = team2 );


