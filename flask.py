import os
from flask import flask
app = flask(__name__)
--
--
colour = os.environ.get ('APP_COLOR')
@app.route =("/")
def main():
print(color)
return render_template('hello.html' ,color=color)
if __name__ = "__main__":
app.run(host="0.0.0.0", port="8080")

