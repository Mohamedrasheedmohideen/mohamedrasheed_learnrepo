import json

file=open('ex5.json')

ex5=json.load(file)
for donut in ex5:
    if donut['name']=='Old Fashioned':
        donut['batters']['batter'].append({"id":"1003","type":"Coffee"})

with open('ex5.json','w') as file:
    json.dump(ex5,file,indent=4)
