#data structure is ["contacts"][index]["name"/"phone_number"/"address"]
from operator import itemgetter
import re

#expects data in the phonebook format
def sort(data, field):
    return sorted(data, key=itemgetter(field))

'''
def sort_addr(data):
    return sorted(data, key=itemgetter("address"))

def sort_phone(data):
    return sorted(data, key=itemgetter("phone_number"))

def sort_lastName(data):
    return sorted(data, key=itemgetter("last_name"))

def sort_firstName(data):
    return sorted(data, key=itemgetter("first_name"))
'''

def filter_data(data, field, search):
    newData = []
    for item in data:
        if (item[field].find(search) > 0):
            newData.append(item)

    return newData
            

#filter by
    #global
    #number contains
    #postcode


