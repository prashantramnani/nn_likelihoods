import json 
  
# Opening JSON file 
f = open('data.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
print(type(data[0]['rt']))
  
# Closing file 
f.close()