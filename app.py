from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def home():
    print("HELLO I AM A FLASK APP")
    return render_template("index.html" , page_name = "WHAT2WATCH")

@app.route("/search")
def search_results():
    return render_template("index.html" , page_name = "SEARCH RESULTS")

app.run(debug =  True)
