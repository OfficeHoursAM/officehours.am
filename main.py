# imports
import flask

# globals
app = flask.Flask(__name__)

# routes
@app.route('/')
def index():
    return flask.render_template("index.html", entries = [
        {
            "title": "The Microtransaction Generation",
            "guest":
            {
                "name": "Alec Davis",
                "href": "http://twitter.com/alecat1008"
            },
            "pubdate": "02.24.14",
            "description": "The 30-year-career is a thing of the past. How has the current economy has helped cause that, what does it mean for the economy in the future? And what does it mean for the millennial generational identity?"
        },
        {
            "title": "Something Economy-y",
            "guest":
            {
                "name": "James Lomuscio",
                "href": "http://hability.net"
            },
            "pubdate": "03.24.14",
            "description": "The 30-year-career is a thing of the past. How has the current economy has helped cause that, what does it mean for the economy in the future? And what does it mean for the millennial generational identity?"
        }
    ])

@app.route('/rss.xml')
def rss():
    pass

# functions
if __name__ == "__main__":
    app.run(debug = True)
