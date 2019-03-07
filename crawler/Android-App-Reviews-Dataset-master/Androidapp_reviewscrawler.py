
import re
import sys
import requests
from lxml import html
import re
import demjson

def get_review(package):

    return_data = {}
    url = 'https://play.google.com/store/apps/details?id='+package+'&hl=en'
    return_data['package'] = package
    comments = []
    while(True):

        try:
            print url
            response = requests.get(url, timeout=1.0)
            break;
        except requests.exceptions.Timeout as e:
            print('Connection Timeout')
        except requests.exceptions.ConnectionError as e:
            print('No Internet connection')
    #parse the body into tree
    text = (response.text).encode("utf8")

    matchobj = re.findall(r'<a itemprop="genre" href="https:\/\/play\.google\.com\/store.*?>([\s\S]*?)<\/a>',text)
    if(len(matchobj) > 0):
        cateory =  matchobj[0]

        matchobj = re.findall(r"<script.*?>([\s\S]*?)<\/script>",text,re.M|re.I)
        
        for sc in matchobj:
            if "key: 'ds:14'" in sc:
                json = re.findall(r"AF_initDataCallback([\s\S]*?);",sc,re.M|re.I)
                jk = json[0].split("return ");
                k = jk[1].replace("}","");
                j = k.replace(")","");
                
                try:
                    k = demjson.decode(j)
                    comment =  k[0][0][4]
                    
                    for comment in k[0]:
                        asd = comment[4].encode("utf8").replace("\n","");
                        comments.append(asd + "*--^--*" + cateory + "\n")
                except Exception,e:
                    print "Exception " + package 
                return comments

    return comments
    

file = open('appid_example',"r")

data_file = open('dataset.txt',"w");

data_set = []

for line in file:
    comments = get_review(line.strip())
    for comment in comments:
        data_file.write(comment) 

data_file.close()

    