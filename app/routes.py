from flask import Flask, render_template, request
from app import app

@app.route('/')
def home_page():
    return render_template('base.html')

@app.route('/favorites', methods = ["GET"])
def favorites():
    """so, i really dont have a top 5 out of artists or athletes so im going to expand the list alittle
    hopefully that is ok

    Returns:
        list: list of top 5 artists, athletes, and other things i like
    """
    top_things = ['NF', 'Justin Fields', 'Darkrai', 'Obi-Wan', 'Cats']
    
    return render_template('favorites.html', top_things = top_things)