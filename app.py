from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import pyshorteners



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(30),nullable =False)
    detail = db.Column(db.String(100))
    due =db.Column(db.DateTime,nullable = False)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/reference')
def reference():
    return render_template('reference.html')

# @app.route('/url')
# def url():
#     return render_template('url.html')

@app.route('/url',methods =['POST','GET'])
def home():
  if request.method=="POST":
    url_received = request.form["url"]
    short_url = pyshorteners.Shortener().tinyurl.short(url_received)
    return render_template('url.html',new_url=short_url, old_url=url_received)
  else:
    return render_template('url.html')

if __name__ == "__main__":
    app.run(debug=True)