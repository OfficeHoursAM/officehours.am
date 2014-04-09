# imports
import flask
import episodes
import requests
from async import async

# globals
app = flask.Flask(__name__)

# routes
@app.route('/')
def index():
    return flask.render_template("index.html", server = flask.request.host, entries = episodes.entries)

@app.route('/rss.xml')
def rss():
    return flask.render_template("rss.xml", server = flask.request.host, entries = episodes.entries)

@app.route('/subscribe')
def subscribe():
    return flask.redirect("pcast://%s/rss.xml" % (flask.request.host), code = 302)

@app.route('/podcasts/<filename>')
def episode(filename):
    if (filename not in episodes.filenames()):
        flask.abort(404)

    for entry in episodes.entries:
        if entry["filename"] == filename:
            episode = entry
            break
    else:
        return flask.abort(404)

    return flask.redirect(episode["href"], code = 302)

# main
if __name__ == "__main__":
    app.run(debug = True)
