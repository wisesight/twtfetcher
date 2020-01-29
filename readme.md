# Twitter fetcher api

### Usage
```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install -r requirements.txt
```

### Set required environment variable
```
$ export CONSUMER_KEY={YOUR_CONSUMER_KEY}
$ export CONSUMER_SECRET={YOUR_CONSUMER_SECRET}
$ export ACCESS_TOKEN={YOUR_ACCESS_TOKEN}
$ export ACCESS_TOKEN_SECRET={YOUR_ACCESS_TOKEN_SECRET}
```

### Start in dev mode
```
$ python api.py
```

### Start in production mode
```
$ uwsgi --ini wsgi.ini
```

### Or start using docker
```
$ docker run -e CONSUMER_KEY={consumer_key} -e CONSUMER_SECRET={consumer_secret} -e ACCESS_TOKEN={access_token} -e ACCESS_TOKEN_SECRET={access_token_secret} -p 5000:5000 wisesight/twtfetcher
```

### Example request
```
$ curl -H 'Content-Type: application/json' -X POST 'http://localhost:5000' -d '{"ids":["example_id_1","example_id_2"]}'
```
