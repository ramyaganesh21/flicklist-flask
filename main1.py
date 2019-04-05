from flask import Flask
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def index():
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    
    movie = get_random_movie()

    content += "<h1>Movie of Tommorrow</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    
    movie = ["The Big Lebowski","Titanic", "Jurrasic Park", "Forest Gump", "Slum Dog Millionaire"]
    return random.choice(movie)



app.run  ()  