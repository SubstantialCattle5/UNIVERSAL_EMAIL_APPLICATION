import json


with open('web_smtp_protocols.json' ,'r' ) as file :
    a = json.load(file)
    print(a['gmail'])