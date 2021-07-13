"""
Description about all imported files
Flask: is the main module for flask functionality
render_template: is used to render the html files present inside the templates folder
url_for: is used to give file name or url only then it will find it automatically
and run it.
"""
from flask import Flask
from flask import render_template
from flask import url_for

"""
Here __name__ is a module(This pertucular python file)
when we run this file/app so we can use this __name__ as a __main__.
"""
app = Flask("__name__")


posts=[
    {
        "author": "Pushpendra Kumar",
        "publish_date":"18/02/1998",
        "title":"this is a title",
        "content":"this is a descritption"
    },
    {
        "author": "Pushpendra Kumar",
        "publish_date":"18/02/1998",
        "title":"this is a second title",
        "content":"this is a second descritption"
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="New page")



if __name__ == "__main__":
    app.run(debug=True)

