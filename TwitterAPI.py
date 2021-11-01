import tweepy

auth = tweepy.OAuthHandler("wDt2i9RC6AAPcl3VmNZXCQS93", "WhVnXmH3l8o9tzflX0vPsp3IudXNBGZ8qRzd4qDLw3jEnlnNaT")
auth.set_access_token("1400315591181967363-0b8WDyP73R04Fn1T0dHs2M0bXDEkW9", "BCYV1UzeQis6RGMOvlCH0P17auA6hoA7SLIup8ODAy13F")

tweet = tweepy.API(auth)

account_tweets = tweet.home_timeline()
for x in account_tweets:
    print(x.user.name+ ": " + x.text)