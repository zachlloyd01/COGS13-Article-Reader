from flask import Flask, render_template, redirect, request, jsonify
from ReadArticles import ReadArticles

from firebase_connection import FBConn

app = Flask(__name__) #Lazyloading

firebase_connection = FBConn()

# @app.route('/') #Root domain
# def home(): #Homepage
#     """ function to return home.html """
#     return render_template('home.html')

@app.route('/')
def articles():

    articles = firebase_connection.getArticles()

    return render_template('articles.html', articles=articles)

@app.route('/feeds')
def feeds():
    feeds = firebase_connection.getFeeds()
    return render_template('feeds.html', feeds=feeds)

@app.route('/addfeed')
def addFeed():
    return render_template('addfeed.html')

@app.route('/createfeed', methods=['POST'])
def createFeed():
    name = request.form['name']
    link = request.form['link']
    
    firebase_connection.addFeed(name, link)

    return redirect('/feeds')

@app.route('/updatearticles')
def updateArticles():
    feeds = firebase_connection.getFeeds()

    feedsList = []

    for feed in feeds:
        feedsList.append({feed: feeds[feed]})

    ReadArticles.readFromLinks(feedsList)

    return jsonify('done')

app.run() #Open webserver
