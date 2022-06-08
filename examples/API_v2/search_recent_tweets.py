import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAABY4TwEAAAAAKRHBh0JJ0YHjlGLYBAkeHH6lb%2BQ%3DiAERZ0SmmAqz5emb8RLU10sKekwnTa0EvhVCfWZaCdnYzcoqBy"

client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("Tweepy")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=100)
