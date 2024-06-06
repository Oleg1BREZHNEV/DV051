from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {

        "link": "Посмотреть фильм Старик и море"
    }
    return render_template("base.html", **context)



@app.route("/home/")
def films3():
    context = {

        "link": "Посмотреть фильм Пляж"
    }
    return render_template("base.html", **context)


@app.route("/about/")
def person():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()