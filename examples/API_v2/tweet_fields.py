import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAABY4TwEAAAAAKRHBh0JJ0YHjlGLYBAkeHH6lb%2BQ%3DiAERZ0SmmAqz5emb8RLU10sKekwnTa0EvhVCfWZaCdnYzcoqBy"

client = tweepy.Client(bearer_token)

# You can specify additional Tweet fields to retrieve using tweet_fields
response = client.search_recent_tweets(
    "Tweepy", tweet_fields=["id", "created_at", "lang", "text", "geo"]
)
tweets = response.data

# You can then access those fields as attributes of the Tweet objects
for tweet in tweets:
    print(tweet.id, tweet.text, tweet.geo, tweet.lang)

# Alternatively, you can also access fields as keys, like a dictionary
for tweet in tweets:
    print(tweet["id"], tweet["lang"])

# There’s also a data attribute/key that provides the entire data dictionary
for tweet in tweets:
    print(tweet.data)
