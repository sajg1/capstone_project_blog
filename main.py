from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/89579a9c020f1d21c96e')
    blog_posts = response.json()
    return render_template("index.html", posts=blog_posts)

@app.route("/blog/<id>/<title>/<subtitle>/<body>")
def get_blog(id, title, subtitle, body):
    return render_template("post.html", post_title=title, post_sub=subtitle, post_bod=body)


if __name__ == "__main__":
    app.run(debug=True)
