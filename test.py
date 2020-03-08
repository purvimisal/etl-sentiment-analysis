import tweepy



consumer_key = "AMJPemK9c7DBeG3NBAUACYuOG"
consumer_secret = 'XykYZckKZlzIXd246QhZEsYS17oNaENfoPyhTFjgVILHTNqZpm'
access_token = '1177331399688253440-gEon1g93X1jmvnJnlrhMwoYhvMIS84'
access_token_secret = 'cRrX66VmyColXaG1NUIH3Et2szfwxyWAHdhXnIwIqbgaK'
password = 'November96#$'






auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()





for tweet in public_tweets:
    print(tweet.text)