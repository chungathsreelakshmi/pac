import pickle
import itertools
import sys
import pprint
#all permission
def get_all_permission():
	all_permission = []
	file = open("all_permission.txt","r");
	for line in file:
		line = line.strip()
		all_permission.append(line)
	file.close()
	return all_permission;

def get_data_set():
	file = open("dataset.pickle","rb")
	apps = pickle.load(file)
	file.close()
	return apps



def get_application_count_for_permission(apps,permision_comb):
	global all_permission
	i = 0
	for app in apps:
		permissions = app[1]['details']['app_details']['permission']
		permissions = set([x.split(".")[-1]  for x in permissions if x.split(".")[-1] in all_permission])
		if set(permision_comb).issubset(permissions):
			i +=1
	return i

frequent_item_set = {}
apps = get_data_set();
all_permission = get_all_permission();

for cat in apps.keys():
	print ("Category: " + cat)
	print("No. Of apps: " + str(len(apps[cat])))
	iteration = []

	# get all permissions of the category
	permissions = []
	for app_ar in apps[cat]:
		app_permissions = app_ar[1]['details']['app_details']['permission']
		app_permissions = [x.split(".")[-1]  for x in app_permissions if x.split(".")[-1] in all_permission]
		for perm in app_permissions:
			if(perm not in permissions):
				permissions.append(perm)
	print ("Total permission count: " + str(len(permissions)))
	if(len(permissions) <= 20 and len(permissions) > 0):
		# create first iteration and remove all permissions not having support 80%
		frequency = {}
		iterobj = itertools.combinations(permissions,1)
		for perm in iterobj:
			count = get_application_count_for_permission(apps[cat],perm)
			frequency[perm] = count
		temp = {}
		for i in frequency:
			# SUPPORT 80%
			if(frequency[i] > len(apps[cat]) * .80):
				temp[i] = frequency[i]
		iteration.append(temp)
		# pprint.pprint(iteration)

		# Update permission with support
		permissions = set()
		for i in temp:
			permissions = permissions.union(set(i))
		# pprint.pprint(permissions)

		# print ("Permission count after supprt: " + str(len(permissions)))

		# Iteration 2 to the combination length
		for i in range(2,len(permissions)+1,1):
			frequency = {}
			pprint.pprint ("Counting for: " + str(i))
			iterobj = itertools.combinations(set(permissions),i)
			for perm_comb in iterobj:
				# print(len(perm_comb))
				count = get_application_count_for_permission(apps[cat],perm_comb)
				frequency[perm_comb] = count

			temp = {}
			for perm_comb in frequency:
				# SUPPORT 80%
				if(frequency[perm_comb] > len(apps[cat]) * .80):
					temp[perm_comb] = frequency[perm_comb]
			iteration.append(temp)
		# pprint.pprint(iteration)
		frequent_item_set[cat] = iteration
	else:
		print("Category"+ " " + cat + " skipped!")
file = open("frequent_item_set.pickle","wb")
pickle.dump(frequent_item_set,file)
file.close()