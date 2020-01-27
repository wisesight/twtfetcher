# Twitter fetcher api

### Usage
```
$ python3 -m venv env
$ source env/bin/activate
$ python -m pip install -r requirements.txt
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
