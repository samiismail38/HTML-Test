from flask import Flask, url_for, render_template

app=Flask(__name__)



@app.route("/")
def home():
    return render_template("test.html")


if __name__=="__main__":
    app.run()