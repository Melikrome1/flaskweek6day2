from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'My Top 5 Favorites Actors'
    favorites = ['Viola Davis', 'Mark Wahlberg','Jason Statom', 'Dwayne Johnson', 'Denzel Washington']
    return render_template('index.html', first_name=name, favorites =  favorites)

@app.route('/test')
def test():
    return render_template
