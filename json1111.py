import json

input = '''[{
    "id": "001",
    "x": 2,
    "name": "Chuck"
    },
    {"id":"009",
    "x": "7",
    "name":"Bridget"
    }
]'''

info2 = json.loads(input)
print('Count:', len(info2))
for item in info2:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
