from application import app,db
from flask import render_template,request,json,Response

courseData = [{"courseID":"1111","title" : "PHP","description" : "Intro to PHP","credits" : "3","term" : "Apache, Lamp"
},{"courseID":"2222","title" : "JAVA","description" : "Intro to Java","credits" : "5","term" : "Spring Boot"
},{"courseID":"3333","title" : "Python","description" : "Intro to Python","credits" : "6","term" : "Flask and Django"
},{"courseID":"4444","title" : "Docker","description" : "Intro to Docker","credits" : "8","term" : "Kubernetas"
},{"courseID":"5555","title" : "Machine Learing","description" : "Intro to ML","credits" : "8","term" : "Automation"
},{"courseID":"6666","title" : "Artificial Intelligence","description" : "Intro to AI","credits" : "10","term" : "Human AI"
}]
@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html",index=True)

@app.route("/login")
def login():
    return render_template("login.html",login=True)

@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term="Spring 2020"):
    
    return render_template("courses.html",courseData=courseData,courses=True,term=term)

@app.route("/register")
def register():
    return render_template("register.html",register=True)

@app.route("/enrollment",methods=["GET","POST"])
def enrollment():
    id = request.form.get('courseID')
    title = request.form['title']
    term = request.form.get('term')
    return render_template("enrollment.html",enrollment=True,data={"id":id,"title":title,"term":term})

@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    return Response(json.dumps(jdata),mimetype="appication/json")

class User(db.Document):
    user_id = db.IntField(unique = True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=30)
    password = db.StringField(max_length=30)

@app.route("/user")
def user():
    User(user_id=1,first_name="Suresh",last_name="Koochana",email="kuchana123.suresh@gmail.com",password="welcome@123").save()
    User(user_id=1,first_name="Swetha",last_name="Koochana",email="suresh123.kuchana@gmail.com",password="welcome@123").save()
    users = User.objects.all()
    return render_template("user.html",users=users) 

