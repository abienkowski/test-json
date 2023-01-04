import json

with open('./test.json', 'r') as f:
  data = json.load(f)

print("Hi, my name is " + data["firstname"])
