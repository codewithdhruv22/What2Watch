from flask import Flask , render_template
import urllib
import json
app = Flask(__name__)


@app.route("/")
def home():
    print("HELLO I AM A FLASK APP")
    return render_template("index.html" , page_name = "WHAT2WATCH")


@app.route("/search/<string:movieName>")
def search_results(movieName):
    url =  f"http://www.omdbapi.com/?s={movieName}&apikey=c4b3701e"
    response = urllib.request.urlopen(url)
    data = response.read()
    jsonData = json.loads(data)["Search"]
    return render_template("index.html" , page_name = "SEARCH RESULTS" , movieList = jsonData)



app.run(debug =  True)
