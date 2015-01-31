'''

This script will fetch someone's timeline from Twitter
and analyze his/her feeling from recent tweets.
Made by: Giri Kuncoro (gk256@cornell.edu)

'''

import twitter
import nltk
import matplotlib.pyplot as plt
import numpy as np

# Twitter requires authorization to access their API
# to get key and access token, go to http://apps.twitter.com/ and create one
api = twitter.Api(consumer_key='2RJYLeeXVWftefdtvkKwIO7Wl', 
                  consumer_secret='3aZefjttWKg5ONDN4Zk6B2fmuCO1i5EZMmsuQf1bTHcA8QJr3Q',
                  access_token_key='136962040-numg6UfhgDhJCLyF1zLoIohN7xqik6DStR0nHNUO',
                  access_token_secret='ofTjnhSaKLxY5s8cPI5gI13xPfnVRCNItc8yIJ4ZjgTTP')

# Getting argument from user's command line input
if __name__ == "__main__":
    import sys
    username = sys.argv[1]
    if len(sys.argv) > 2:
    	numberOfTweet = sys.argv[2]
    else:
    	numberOfTweet = 100 # default number of tweets

# Function to fetch user's timeline data
def fetchTweet(user):
	numbers = numberOfTweet
	statuses = api.GetUserTimeline(screen_name = user, count = numbers)

	tweet = ""
	for s in statuses:
	    tweet = tweet + s.text
	return tweet

# Fetch the user's timeline
tweets = fetchTweet(username)

# Define dictionary for feeling, I need to insert more words to make it more interesting
feelingCount = {'positive': 0, 'happy': 0, 'lovely': 0, 'negative': 0, 'sad': 0, 'angry': 0, 'sick': 0}
feelingWords = {}

feelingWords['positive'] = [
'excellent', 'amazing', 'beautiful', 'nice', 'marvelous', 'magnificent', 'fabulous', 'astonishing', 'fantastic', 'peaceful', 'fortunate',
'brilliant', 'glorious', 'cheerful', 'gracious', 'grateful', 'splendid', 'superb', 'honorable', 'thankful', 'inspirational',
'ecstatic', 'victorious', 'virtuous', 'proud', 'wonderful', 'lovely', 'delightful']

feelingWords['happy'] = [
'happy', 'lucky', 'awesome', 'excited', 'fun', 'amusing', 'amused', 'pleasant', 'pleasing', 'glad', 'enjoy',
'jolly', 'delightful', 'joyful', 'joyous', ':-)', ':)', ':-D', ':D', '=)']

feelingWords['lovely'] = [
'love', 'adore', 'blissful', 'heartfelt', 'loving', 'lovable', 'sweetheart', 'darling', 'kawaii', 'married', 'engaged']

feelingWords['negative'] = [
'unhappy', 'bad', 'sorry', 'annoyed', 'dislike', 'anxious', 'ashamed', 'cranky', 'crap', 'crappy', 'envy',
'awful', 'bored', 'boring', 'bothersome', 'bummed', 'burned', 'chaotic', 'defeated', 'devastated', 'stressed',
'disconnected', 'discouraged', 'dishonest', 'doomed', 'dreadful', 'embarrassed', 'evicted', 'freaked out', 'frustrated', 'stupid',
'guilty', 'hopeless', 'horrible', 'horrified', 'humiliated', 'ignorant', 'inhumane', 'cruel', 'insane', 'insecure',
'nervous', 'offended', 'oppressed', 'overwhelmed', 'pathetic', 'powerless', 'poor', 'resentful', 'robbed', 'screwed']

feelingWords['sad'] = [
'sad', 'alone', 'anxious', 'depressed', 'disappointed', 'disappointing', 'sigh', 'sobbing', 'crying', 'cried',
'dumped', 'heartbroken', 'helpless', 'hurt', 'miserable', 'misunderstood', 'suicidal', ':-(', ':(', '=(', ';(']

feelingWords['angry'] = [
'hate', 'damn', 'angry', 'betrayed', 'bitched','disgust', 'disturbed', 'furious', 'harassed', 'hateful', 'hostile', 'insulted',
'irritable', 'jealous', ' rage ', 'pissed']

feelingWords['sick'] = [
'sick', ' ill ', 'under weather', 'throw up', 'threw up', 'throwing up', 'puke', 'puking', 'pain', 'hangover', 'intoxicated']

# Analyze feeling from user's most recent tweets
# NLTK library is used
for words in feelingWords:
    for feel in feelingWords[words]:
        if tweets.find(feel) > 0:
            if words == 'positive':
                feelingCount['positive'] = feelingCount['positive'] + 1
            elif words == 'happy':
                feelingCount['happy'] = feelingCount['happy'] + 1
            elif words == 'lovely':
                feelingCount['lovely'] = feelingCount['lovely'] + 1
            elif words == 'negative':
                feelingCount['negative'] = feelingCount['negative'] + 1
            elif words == 'sad':
                feelingCount['sad'] = feelingCount['sad'] + 1
            elif words == 'angry':
                feelingCount['angry'] = feelingCount['angry'] + 1
            elif words == 'sick':
                feelingCount['sick'] = feelingCount['sick'] + 1

# matplotlib is used to plot user's feeling
y_pos = np.arange(len(feelingCount.keys()))
emotion = feelingCount.values()

plt.barh(y_pos, emotion, align='center', alpha=0.4)
plt.yticks(y_pos, feelingCount.keys())
plt.xlabel('Emotion level')
plt.title('Analyzing @' + sys.argv[1] + '\'s feeling from ' + str(numberOfTweet) + ' recent tweets')

# Show the plotted feeling
plt.show()