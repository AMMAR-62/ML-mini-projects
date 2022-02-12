# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creds


"""TWITTER STREAM LISTENER: basic listener, appends received tweets to files"""
class StdOutListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            if(self.fetched_tweets_filename):
                with open(self.fetched_tweets_filename, 'a') as tf:
                    tf.write(data)
                return True
            else:
                print(data)
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
"""TWITTER STREAMER: streaming and processing live tweets"""
class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(creds.CONSUMER_KEY, creds.CONSUMER_SECRET)
        auth.set_access_token(creds.ACCESS_TOKEN, creds.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    hash_tag_list = ["Modi", "Amit Shah", "BJP", "Uddhav Thackeray"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)