import database as db
import re
import pickle
import uuid
import requests as req
import demjson
from flask import Flask,render_template,request,redirect,session,url_for,flash
from api import api


app=Flask(__name__)
app.secret_key="zdszcsdjcsdckshnsdsefe"
app.register_blueprint(api)

@app.route('/',methods=['get','post'])
def homepage():
    return render_template('Homepage.html')

@app.route('/login/',methods=['get','post'])
def login():
    if "login" in request.form:
        username=request.form['username']
        password=request.form['password']
        result=db.select("select * from tbl_login where username='%s' and password='%s'" %(username,password))

        if(len(result)>0):
            session['id']=result[0]['login_id']
            print (session['id'])
            if result[0]['user_type']=='admin':

                #flash("Login Successfull !!!")
                return redirect(url_for('admin_home'))
            else:
                flash("invalid username")
        return render_template('login.html',error_message="Incorrect Username/Password !!!")
    return render_template('login.html')

@app.route('/Admin_home/',methods=['get','post'])
def admin_home():

    if "id" in session:
        return render_template('Admin_home.html')
    else:
        return redirect(url_for('login'))

@app.route('/Admin_view_category/',methods=['get','post'])
def Admin_view_category():
    if "id" in session:
        file = open("dataset/frequent_item_set.pickle","rb")
        data = pickle.load(file)
        file.close()
        return render_template('view_category.html',data=data)
    else:
        return redirect(url_for('login'))
@app.route('/view_category_frequent_list/',methods=['get','post'])
def view_category_frequent_list():
    if "id" in session:
        category = request.args['category']
        file = open("dataset/frequent_item_set.pickle","rb")
        data = pickle.load(file)
        file.close()
        return render_template('view_frequency.html',data=data[category])
    else:
        return redirect(url_for('login'))


@app.route('/View_users/',methods=['get','post'])
def view_users():
    if "block" in request.args:
        u_id = request.args['id']
        q = "update tbl_login  set login_status='block' where login_id='%s'"%u_id
        db.update(q)
    if "unblock" in request.args:
        u_id = request.args['id']
        q = "update tbl_login  set login_status='Active' where login_id='%s'"%u_id
        db.update(q)
    # result=db.select("select u.*,lo.login_status from tbl_users u,tbl_login lo where u.login_id=lo.login_id")
    result=db.select("SELECT * FROM tbl_login INNER JOIN tbl_users USING (login_id) WHERE login_status='active'")
    result1=db.select("SELECT * FROM tbl_login INNER JOIN tbl_users USING (login_id) WHERE login_status='block'")
    return render_template('View_users.html',data=result,data1=result1)

@app.route('/logout/',methods=['get','post'])
def logout():
    session.clear()
    return redirect(url_for('homepage'))

@app.route('/test_an_app/',methods=['get','post'])
def test_an_app():
    result = ''
    if "upload" in request.form:
        file = request.files['manifest']
        filename  = "uploads/" +str(uuid.uuid4()) + ".xml"
        file.save(filename)
        data = {
            "path" : filename
        }
        response = req.post(url ="http://" + str(request.host) + "/api/check_permision_abuse/", data = data)
        print(response.text)
        result = demjson.decode(response.text)
    return render_template('test_an_app.html',data = result)
            

app.run(debug=True,port=5001,host="192.168.1.76")