import re
import sys
import urllib
import re
import demjson
import pickle
import uuid
import os
import database as db
import pprint

from flask import Blueprint,request,redirect,url_for,render_template

api = Blueprint('api',__name__)

def permission_abuse(permission_set,cat):
	file = open("dataset/frequent_item_set.pickle","rb")
	frequent_item_set = pickle.load(file)
	file.close()
	n = len(permission_set)
	result = {}
	total_set = set([])
	if cat  in frequent_item_set:
		for iteration in frequent_item_set[cat] :
			if(len(list(iteration.keys())[0]) == n):
				total_set = total_set.union(list(iteration.keys())[0])
				intersection = []
				for i in list(iteration.keys()):
					if(set(permission_set).issubset(set(i))):
						result['abuse'] = "no"
						result['abused_permission'] = ""
						result['permissions'] = permission_set
						return result
		
		result['abuse'] = "yes"
		result['abused_permission'] = set(permission_set) - total_set.intersection(set(permission_set))
		result['permissions'] = permission_set
	else:
		result['abuse'] = "failed"
		result['reason'] = "Category not found in frequent set"
	return result

@api.route('/api/check_permision_abuse/',methods=['get','post'])
def check_permision_abuse():
	def get_category(package):
		url = 'https://play.google.com/store/apps/details?id='+package+'&hl=en'
		f = urllib.request.urlopen(url)
		text = (f.read()).decode("utf-8")
		cateory = None
		matchobj = re.findall(r'<a itemprop="genre" href="https:\/\/play\.google\.com\/store.*?>([\s\S]*?)<\/a>',text)
		if(len(matchobj) > 0):
			cateory =  matchobj[0]
		return cateory

	

	if "path" in request.form:
		filename = request.form['path']
	else:	
		filename  = "uploads/" +str(uuid.uuid4()) + ".xml"
		file = request.files['manifest']
		file.save(filename)

	file = open(filename,"r")

	permissions = []
	for line in file:
		group_obj = re.findall('<uses-permission android:name="android.permission.(.*)" />',line)
		package_group = re.findall('package="(.*)"',line)
		if(len(package_group) > 0):
			package = package_group[0];
			cateory = get_category(package)
			cateory = cateory.upper()
			# cateory = 'PRODUCTIVITY'
		if(len(group_obj) > 0):
			permissions.append(group_obj[0]);
	file.close()
	os.remove(filename)
	print(cateory)
	return  demjson.encode(permission_abuse(permissions,cateory))



@api.route('/api/check_permission_abuse_android/',methods=['get','post'])
def check_permision_abuse_android():
	def get_category(package):
		url = 'https://play.google.com/store/apps/details?id='+package+'&hl=en'
		f = urllib.request.urlopen(url)
		text = (f.read()).decode("utf-8")
		cateory = None
		matchobj = re.findall(r'<a itemprop="genre" href="https:\/\/play\.google\.com\/store.*?>([\s\S]*?)<\/a>',text)
		if(len(matchobj) > 0):
			cateory =  matchobj[0]
		return cateory
	permissions = []

	for permission in request.args['permissions'].split(","):
		permissions.append(permission.replace("android.permission.",""))
	permissions = permissions[0:len(permission)-1]
	package = request.args['package_name']
	cateory = get_category(package)
	cateory = cateory.upper()
	print(cateory)

	return demjson.encode(permission_abuse(permissions,cateory))

@api.route('/api/register/')
def register():
	data = {}
	u_fname = request.args['u_fname']
	u_lname = request.args['u_lname']
	u_dob = request.args['u_dob']
	u_phone = request.args['u_phone']
	u_email = request.args['u_email']
	username = request.args['username']
	password = request.args['password']
	q = "insert into tbl_login (username,password,user_type,login_status)values('%s','%s','%s','%s')" %(username,password,'user','Active')
	login_id = db.insert(q)
	q = "insert into tbl_users(login_id,u_fname,u_lname,u_dob,u_phone,u_email)values('%s','%s','%s','%s','%s','%s')" % (login_id,u_fname,u_lname,u_dob,u_phone,u_email)
	k = db.insert(q)
	if (k > 0):
		data['status'] = 'success'
	else:
		data['status'] = 'failed'

	print(data)
	return demjson.encode(data)




@api.route('/api/login/')
def login():
	data = {}
	username = request.args['username']
	password = request.args['password']
	q = "select * from tbl_login where username='%s' and password='%s' and login_status='Active'" % (username,password)
	result = db.select(q)
	if(len(result) > 0):
		data['status'] = "success"
		data['login_data'] = result[0]
	else:
		data['status'] = 'failed'
	print(data)
	return demjson.encode(data)
