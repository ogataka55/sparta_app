from flask import Flask, render_template, request, redirect, url_for

import db

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/index")
def index():
    posts = db.get_all_posts()

    return render_template("index.html", posts=posts)


@app.route("/add", methods=["POST"])
def add_post():
    """新規投稿を追加する関数"""
    title = request.form["title"]
    detail = request.form["detail"]

    if not title or not detail:
        return redirect(url_for("index"))
    else:
        db.add_post(title, detail)

    return redirect(url_for("index"))


@app.route("/view/<int:id>")
def detail(id):
    return render_template("view.html", id=id)


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
