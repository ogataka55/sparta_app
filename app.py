from flask import Flask, render_template

import db

app = Flask(__name__)


@app.route("/index")
def index():
    customers = db.get_all_customers()

    return render_template("index.html", customers=customers)


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
