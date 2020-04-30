import urllib.request, urllib.parse, urllib.error
import json

# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_458724.json

address = input("Enter webite: ")
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print("Retrieved", len(data), 'characters')

js = json.loads(data)
#print(data)

counter = 0
for item in js["comments"]:
    #print(item["count"])
    counter = counter +int(item["count"])

print(counter)
