from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route("/")
def index():
    # displays 8x8 checkerboard
    return render_template("index.html", row=8, col=8, color1="orange", color2 = "palegoldenrod")

@app.route("/<int:col>")
def eight_by_col(col):
    # Displays 8xnum checkerboard
    return render_template("index.html",row=8,col=col, color1="orange",color2="palegoldenrod")

@app.route("/<int:row>/<int:col>")
def x_and_y(row,col):
    # displays row x col checkerboard
    return render_template("index.html",row=row,col=col, color1="orange",color2="palegoldenrod")

@app.route("/<int:row>/<int:col>/<string:col_1>/<string:col_2>")
def checker_colors(row,col,col_1,col_2):
    # displays a checkerboard with rows x col and alternating color1 and color 2
    print("hi")
    return render_template("index.html",row=row,col=col,color1=col_1,color2=col_2)

if __name__== "__main__":
    app.run(debug=True)

# For macs, remember to add port = 5001 << something like this check the platform