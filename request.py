import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Date':1, 'Rented Bike Count':2, 'Hour':3,'Temparature(C)':4,'Humidity(%)':5 ,
'Wind Speed(m/s)':6 ,'Visibilty(10m)':7 ,'Dew point temperature(C) ':8 ,'Solar Radiation (MJ/m2)':9 ,'Rainfall(mm)':10,
'Snowfall(cm)':11,'Seasons':12, 'Holiday':13, 'Functioning Day':14  })

print(r.json())



  
