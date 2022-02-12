import os

from flask import Flask, render_template, request, redirect, url_for

import db

# ファイルの保存 ./ ⇒ ベースの位置( ~￥sparta_app)
UPLOAD_FOLDER = './static/image'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/index")
def index():
    posts = db.get_all_posts()

    return render_template("index.html", posts=posts)


@app.route("/add", methods=["POST"])
def add_post():
    """新規投稿を追加する関数"""
    title = request.form["title"]
    detail = request.form["detail"]
    img = request.files['image']
    link = request.form['link']

    if img and allowed_file(img.filename):
        filename = img.filename
        # ファイルの保存
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if not title or not detail or not img:
        return redirect(url_for("index"))
    else:
        db.add_post(title, detail, img.filename, link)

    return redirect(url_for("index"))


@app.route("/view/<int:id>")
def view(id):
    post = db.get_one_post(id)
    return render_template("view.html", post=post)


@app.route("/view/<int:id>/view_edit")
def view_edit(id):
    post = db.get_one_post(id)
    return render_template("edit.html", post=post)


@app.route("/view/<int:id>/edit", methods=["POST"])
def edit(id):
    n_title = request.form["n_title"]
    n_detail = request.form["n_detail"]
    n_img = request.files['n_image']
    n_link = request.form['n_link']

    if n_img and allowed_file(n_img.filename):
        filename = n_img.filename
        # ファイルの保存
        n_img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if not n_title or not n_detail or not n_img:
        return redirect(url_for("view", id=id))
    else:
        db.edit_post(id, n_title, n_detail, n_img, n_link)

    return redirect(url_for("view", id=id))


@app.route("/view/<int:id>/delete", methods=['POST'])
def delete(id):
    db.delete(id)
    return redirect(url_for("index"))


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
