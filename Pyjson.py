import json

file=open('exp5.json')

exp5=json.load(file)
for donut in exp5:
    if donut['name']=='Old Fashioned':
        donut['batters']['batter'].append({"id":"1003","type":"Coffee"})

with open('exp5.json','w') as file:
    json.dump(exp5,file,indent=4)
