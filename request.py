import requests



url = 'http://localhost:5000/api/predict'
r = requests.post(url,json={'instances':[0.5,4,629, 0,1,1,0,]})
print(r.json())