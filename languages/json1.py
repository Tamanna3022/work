import json

#dumps method
python_data = {'name':'tamanna', 'roll':22}
#print(python_data)
json_data = json.dumps(python_data)
#print("hello")
#print(python_data)
print(json_data) 



#loads method
a = {"a":"1", "b":"2"}
print(type(a))

if isinstance(a, str):
    a = json.loads(a)
    print(a)
else:
    print(a)

