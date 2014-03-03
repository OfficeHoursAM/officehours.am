# imports
import flask
import episodes
import requests
from async import async

# globals
app = flask.Flask(__name__)
files = {}

# functions
@async
def addEpisode(filename):
    episodeReseponse = requests.get(episodes.fileURLFormat % (filename))
    files.update({episodeReseponse.url: episodeReseponse.content})

    if len(files) == len(episodes.filenames()):
        print "Done!"

# routes
@app.route('/')
def index():
    return flask.render_template("index.html")

@app.route('/setup')
def setup():
    for filename in episodes.filenames():
        addEpisode(filename)

    return ""

@app.route('/rss.xml')
def rss():
    return flask.render_template("rss.xml", server = flask.request.host, entries = episodes.entries)

@app.route('/podcasts/<filename>')
def episode(filename):
    if (filename not in episodes.filenames()):
        flask.abort(404)

    episodeURL = episodes.fileURLFormat % (filename)
    if episodeURL not in files:
        flask.abort(400)

    return flask.Response(files[episodeURL], mimetype = "audio/x-m4a")

# main
if __name__ == "__main__":
    app.run(debug = True)
