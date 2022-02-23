from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/89579a9c020f1d21c96e')
posts = response.json()
blog_posts = []
for post in posts:
    new_post = Post(post['id'], post['title'], post['subtitle'], post['body'])
    blog_posts.append(new_post)

@app.route('/')
def home():
    print(type(blog_posts[0]))
    return render_template("index.html", posts=blog_posts)

@app.route("/blog/<int:id>")
def get_blog(id):
    requested_post = None
    for post in blog_posts:
        if post.get_id() == id:
            requested_post = post
    return render_template('post.html', post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)
