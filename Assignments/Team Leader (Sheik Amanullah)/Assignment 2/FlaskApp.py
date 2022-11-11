from flask import Flask, redirect, url_for, render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qpm23984;PWD=XaDaPlC4zHfFcbX7",'','')
app = Flask(__name__)
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///names.sqlite3'

db = SQLAlchemy(app)
class names(db.Model):
   id = db.Column( db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   email= db.Column(db.String(50))  
   password = db.Column(db.String(200))
 
def __init__(self, name, email, password):
   self.name = name
   self.email = email
   self.password = password

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/new')
def new():
    return render_template('new.html',names = names.query.all())

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup" ,methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
       if not request.form['name'] or not request.form['email'] or not request.form['password']:
          flash('Please enter all the fields', 'error')
       else:
         name = names(request.form['name'], request.form['email'],request.form['passowrd'])
         
         db.session.add(name)
         db.session.commit()
         
         flash('Record was successfully added')
        
         return redirect(url_for('new')) 
        
    return render_template("signup.html")

@app.route("/aboutpage")
def aboutpage():
    return render_template("aboutpage.html")


if __name__ == "__main__":
    db.create_all()
    app.run()
 

