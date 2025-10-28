from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Flask入門",
        heading="テンプレートによる描画",
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

if __name__ == "__main__":
    app.run(debug=False)
