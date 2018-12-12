# DeliveryHero

# 1 Setup 

* Create virtualenv (I used Python 3.6)
* ```pip install -r requirements.txt```

# 2 Run
*```python Run.py```

# 3 Use (Examples)

* POST (Create a Restaurant)
```
curl -X POST \
  http://0.0.0.0:5000/restaurant \
  -F 'restaurant={"name": "Da Rosario",
  "opens_at": "2018-01-10 08:15:00.000000",
  "closes_at": "2018-09-29 20:15:20.000000"}
  '
```

* GET (Retrieve a Restaurant)
```
curl -X GET \
  http://0.0.0.0:5000/restaurant/1
```

* PUT (Update a Restaurant)
```
curl -X PUT \
  http://0.0.0.0:5000/restaurant/1 \
  -F 'restaurant={"name": "Da Rosario2",
  "opens_at": "2018-01-10 08:15:00.000000",
  "closes_at": "2018-09-29 20:15:20.000000"}
  '
```

* DELETE (Delete a Restaurant)
```
curl -X DELETE \
  http://0.0.0.0:5000/restaurant/2
```
