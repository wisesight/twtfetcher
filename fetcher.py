import tweepy


class Fetcher(object):
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret
    ):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True)

    def fetch(self, ids):
        if len(ids) > 100:
            raise MaxIdsLimitException("Cannot fetch tweet more than 100 at a time")
        response = []
        tweets = self.api.statuses_lookup(ids)
        for tweet in tweets:
            response.append(tweet._json)
        return response


class MaxIdsLimitException(Exception):
    def __init__(self, message):
        super().__init__(message)
