from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main.html")


@app.route('/yes/')
def yes():
    return render_template("yes.html")

@app.route('/no_1/')
def no_1():
    return render_template("no_1.html")

@app.route('/no_2/')
def no_2():
    return render_template("no_2.html")

@app.route('/no_3/')
def no_3():
    return render_template("no_3.html")

@app.route('/no_4/')
def no_4():
    return render_template("no_4.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)