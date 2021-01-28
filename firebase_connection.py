import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class FBConn:
    def __init__(self):

        self.cred = credentials.Certificate('admin_key.json')

        # Initialize the app with a service account, granting admin privileges
        try:
            firebase_admin.initialize_app(self.cred, {
                'databaseURL': 'https://cogs13-project-default-rtdb.firebaseio.com/'
            })
        except:
            print('app already created')
        self.ref = db.reference('/')
        self.article_ref = self.ref.child('articles')
        self.feed_ref = self.ref.child('feeds')


    def addArticle(self, keyPhrase, article):
        ''' Function to create article in the database '''
        title = article['title']
        link = article['link']
        snippet = article['snippet']
        self.article_ref.child(keyPhrase).push({
            'title': title,
            'link': link,
            'snippet': snippet
        })

    def addFeed(self, feedName, feedURL):
        ''' Function to create article in the database '''
        self.feed_ref.child(feedName).set({
            'url': feedURL
        })

    def getFeeds(self):
        ''' Function to return all feeds in the database '''
        return db.reference('feeds').get()

    def getArticles(self):
        ''' Function to return all articles in the database '''
        return db.reference('articles').get()



    

