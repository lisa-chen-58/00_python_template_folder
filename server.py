from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route("/")
def groot():
    return render_template("index.html")

# Insert routes



if __name__== "__main__":
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform