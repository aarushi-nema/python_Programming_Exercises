
#JSON- JavaScript Object Notation
#Json is a data exchange format like XML
#Data is in Key Value pairs
#JSON is light-weight compared to XML

#We will create two programs:
#1. Create an address book and write some records into it
#2. Read this address book

#Let us import the json module
import json

#Let us create a dictionary which will store the address book info
addressBook = {}

#entry 1
addressBook['tom'] = {
    'name' : 'Tom',
    'address': '1 Red Street',
    'phone': '23232323'
}

#entry 2
addressBook['bob'] = {
    'name' : 'Bob',
    'address': '2 Green Street',
    'phone': '474747477'
}

#dumps will first convert the dictionary to a string and then to json format
jsonAddressBook = json.dumps(addressBook)

#Now we'll write the json string a file
with open('/home/ajay/Desktop/python_practice/PythonJson/addressBook.txt', 'w') as addressBookFile:
    addressBookFile.write(jsonAddressBook) 

#You can now read this JSON data using any programming language that supports json such as javascript, c++, etc. 