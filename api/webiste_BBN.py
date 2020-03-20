"""
This program creates a website for Bincy Baburaj Narath. Gives an intro. Feteches Information from Linkedin Profile, Git Hub, and Word Press
"""
import flask
from flask import request, jsonify
import sqlite3

#Initiate flask WSGI
app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def front_page():
	return '''<!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Template</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}

/* Style the header */
header {
  background-color: #ADD8E6;
  padding: 30px;
  text-align: center;
  font-size: 35px;
  color: white;
}

/* Container for flexboxes */
section {
  display: -webkit-flex;
  display: flex;
}

/* Style the navigation menu */
nav {
  -webkit-flex: 1;
  -ms-flex: 1;
  flex: 1;
  background: hotpink;
  padding: 20px;
}

/* Style the list inside the menu */
nav ul {
  list-style-type: none;
  padding: 0;
}

/* Style the content */
article {
  -webkit-flex: 3;
  -ms-flex: 3;
  flex: 3;
  background-color: lavender;
  padding: 10px;
}

/* Style the Links Section*/
links {
  background-color: aliceblue;
  padding: 0px;
  text-align: center;
  color: black;
}

/* Style the footer */
footer {
  background-color: #ADD8E6;
  padding: 10px;
  text-align: center;
  color: white;
}

/* Style the image */
img {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 150px;
}

img:hover {
  box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}

/* Responsive layout - makes the menu and the content (inside the section) sit on top of each other instead of next to each other */
@media (max-width: 600px) {
  section {
    -webkit-flex-direction: column;
    flex-direction: column;
  }
}
</style>
</head>
<body>

<header>
  <h2>Bincy Narath</h2>
</header>

<section>
  <nav>
  	
  </nav>
  <article>
    <h1>Hi There !!</h1>
    <p>Thanks for visiting my page. I am an enthusistic Machine Learning Engineer who is excited about everything logical, fascinated about analytics, enjoys mathematics and coding. Please reach out to me at bincybaburajnarath@gmail.com for any exciting work!</p>
    <p>You can reach out to me for a cup of coffee too. I don't mind as long as you are ready to pay :)</p>
  </article>
</section>

<links>
  <p>I am in Social Media too</p>
  <p>Linkedin</p>
  <p>Facebook</p>
  <p>GitHub</p>
  <p>WordPress</p>
</links>

<footer>
  <p>"It is just the matter of time !"</p>
</footer>

</body>
</html>
'''

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>You clicked something terrible.</p>", 404

app.run(host='192.168.1.174')
