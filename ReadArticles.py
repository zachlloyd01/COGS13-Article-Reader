import feedparser

from firebase_connection import FBConn

firebase_connection = FBConn()
class ReadArticles:
    def readFromLinks(feeds):
        for feed in feeds:
            name = list(feed.keys())[0]
            url = feed[name]['url']
            articles = feedparser.parse(url)

            for entry in articles.entries:
                article = {
                    'title': entry.title,
                    'link': entry.link,
                    'snippet': entry.summary
                }

                firebase_connection.addArticle(name, article)

                
