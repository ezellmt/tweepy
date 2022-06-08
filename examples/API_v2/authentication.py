import tweepy

# Your app's bearer token can be found under the Authentication Tokens section
# of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
bearer_token = "AAAAAAAAAAAAAAAAAAAAABY4TwEAAAAAKRHBh0JJ0YHjlGLYBAkeHH6lb%2BQ%3DiAERZ0SmmAqz5emb8RLU10sKekwnTa0EvhVCfWZaCdnYzcoqBy"

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "n7a9m8C1WW7PMyAb6SU2RQOAS"
consumer_secret = "pxdm1vDd5fEDWGaHq0IhQHPvBUgsJIRjXUzzBWdEpcfZ4ENyvc"

# Your account's (the app owner's account's) access token and secret for your
# app can be found under the Authentication Tokens section of the
# Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
access_token = "90438849-lB47pWSL0KodQ7CtMtFQwNxomrpczO5w3F3zbULIh"
access_token_secret = "87kRfLEDQbBUaoKQw6f4Zjo38hZNhPe0NecxxrJFYFApy"

# You can authenticate as your app with just your bearer token
client = tweepy.Client(bearer_token=bearer_token)

# You can provide the consumer key and secret with the access token and access
# token secret to authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
