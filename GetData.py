from urllib import request
import json 

#get json data from string extracting the contents node
def getPhonebookData():
    webString = ""
    decodeString = ""

    with request.urlopen('http://www.mocky.io/v2/581335f71000004204abaf83') as source:
        webString = source.read()
        decodeString = webString.decode() #convert binary web content to a string

    data = json.loads(decodeString)

    #The iterator returns the dictionary, not the index of the dictionary
    for index in data["contacts"]:
        splitNames = index["name"].split()
        index["last_name"] = splitNames[1]
        index["first_name"] = splitNames[0]
    
    return data["contacts"]






