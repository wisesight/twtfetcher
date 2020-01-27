import flask
import fetcher
import sys
import os

consumer_key = os.getenv('CONSUMER_KEY', None)
consumer_secret = os.getenv('CONSUMER_SECRET', None)
access_token = os.getenv('ACCESS_TOKEN', None)
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET', None)

if consumer_key is None or consumer_secret is None or access_token is None or access_token_secret is None:
    print('No credentials provided')
    sys.exit(1)

fetcher = fetcher.Fetcher(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handler():
    if flask.request.method == 'GET':
        return {'status': 'ok'}, 200
    else:
        if flask.request.json is None:
            app.logger.error('POST req without req body received')
            return {'status': 'error'}, 500
        else:
            try:
                ids = flask.request.json['ids']
                tweets = fetcher.fetch(ids)
                app.logger.info('POST req with req body success')
                return {'status': 'ok', 'data': tweets}, 200
            except Exception:
                app.logger.error('POST req with req body failed')
                return {'status': 'error'}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

