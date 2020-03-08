import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os
import subprocess

# importing file which sets env variable
subprocess.call("./settings.sh", shell=True)
print('successful call')


print(os.environ)
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
password = os.environ.get('PASSWORD')






# consumer_key = "AMJPemK9c7DBeG3NBAUACYuOG"
# consumer_secret = 'XykYZckKZlzIXd246QhZEsYS17oNaENfoPyhTFjgVILHTNqZpm'
# access_token = '1177331399688253440-gEon1g93X1jmvnJnlrhMwoYhvMIS84'
# access_token_secret = 'cRrX66VmyColXaG1NUIH3Et2szfwxyWAHdhXnIwIqbgaK'
# password = 'November96#$'

print(consumer_key,consumer_secret,access_token,access_token_secret)


def connect(id, username, created_at, tweet, retweet_count, place, location):
	"""
	connect to MySQL database and insert twitter data
	"""
	try:
		con = mysql.connector.connect(host='localhost',
		database='twitterdb', user='purvi', password=password, charset='utf8')

		if con.is_connected():
			"""
			Insert twitter data
			"""
			cursor = con.cursor()
			# twitter, golf
			query = "INSERT INTO tweets (id, username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			cursor.execute(query, (id, username, created_at, tweet, retweet_count, place, location))
			con.commit()
			print('INSERTED!!!!!!!!!!!!!!')


	except Error as e:
		print(e)

	cursor.close()
	con.close()

	return


# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):

	def on_connect(self):
		print("You are connected to the Twitter API")

	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""

	def on_data(self, data):

		try:
			raw_data = json.loads(data)
			# print('RAW DATA',raw_data)

			if 'text' in raw_data:
				username = raw_data['user']['screen_name']
				id = raw_data['id_str']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None

				location = raw_data['user']['location']

				# insert data just collected into MySQL database
				connect(id, username, created_at, tweet, retweet_count, place, location)
				# print('THISSSSSSSSSSSSSSSSSSSSSs', id, username, created_at, tweet, retweet_count, place, location)

				print("Tweet collected at: {} ".format(str(created_at)))
		except Error as e:
			print(e)





if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    listener = Streamlistener(api =api)
    stream = tweepy.Stream(auth, listener = listener)
    track = ['cheese', 'food']
    
    stream.filter(track = 'cheese')





	# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)	


	# # # #Allow user input
	# # track = []
	# # while True:

	# # 	input1  = input("what do you want to collect tweets on?: ")
	# # 	track.append(input1)

	# # 	input2 = input("Do you wish to enter another word? y/n ")
	# # 	if input2 == 'n' or input2 == 'N':
	# # 		break

	# # print("You want to search for {}".format(track))
	# # print("Initialising Connection to Twitter API....")
	# # time.sleep(2)

	# # authentification so we can access twitter
    # api = tweepy.API(auth, wait_on_rate_limit=True)
    # listener = Streamlistener(api = api)
    # stream = tweepy.Stream(auth, listener = listener)
    # print('line 121')
    # # print('line 117')


	# # create instance of Streamlistener


	# track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
	# # track = ['nba', 'cavs', 'celtics', 'basketball']
	# # choose what we want to filter by
	# stream.filter(track = track, languages = ['en'])