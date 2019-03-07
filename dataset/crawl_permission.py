import demjson
import urllib3
import pickle
filename = "45_set.txt"

permision_set = []

data = ""

def read_file(filename):
	json_obj = ""
	with open (filename, "r") as myfile:
		json_string=myfile.read().replace('\n', '')
		json_obj = demjson.decode(json_string)
	return json_obj

def download_data_obj(url):
	http = urllib3.PoolManager()
	r = http.request('GET',url)
	data = (r.data).decode("utf8")
	print(data)
	d = ""
	for line in data:
		d += line
	data=d.replace('\n', '')
	json_obj = demjson.decode(data)
	return json_obj

def get_application_permission(metadata_url):
	json_obj = download_data_obj(metadata_url)
	return  json_obj

categories = []
apps = {}
json_obj = read_file(filename)

i = 0
for obj in json_obj:
	cat = obj['category']
	if(cat not in categories):
			categories.append(cat)
	else:
		if cat not in apps:
			apps[cat] = []
		else:
			try:
				app_data = get_application_permission(obj['metadata_url']);
				apps[cat].append([obj,app_data])
			except Exception as e:
				print (e.message)
				pass

	i += 1
file = open("bdataset.pickle","wb")
pickle.dump(apps,file)
file.close()
# print apps[categories[0]]
# print categories
