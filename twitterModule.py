import sys, tweepy, time

consumerKey = "Your consumerKey here!"
consumerSecret = "Your consumerSecret here!"
accessToken = "Your accessToken here!"
accessTokenSecret = "Your accessTokenSecret here!"

def login(consumerKey, consumerSecret, accessToken, accessTokenSecret):
    auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
    auth.set_access_token(accessToken,accessTokenSecret)
    api = tweepy.API(auth)
    return api

def tweet(tweet):
    apii = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    apii.update_status(tweet)
    print("Successfully tweeted. \n")
    main()

def delete_tweets():
    apii = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    timeline = tweepy.Cursor(apii.user_timeline).items()
    for status in timeline:
        apii.destroy_status(status.id)
        time.sleep(1)
    print("All tweets have been deleted. \n")
    main()

def follow(username):
    apii = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    apii.create_friendship(username)
    print("Successfully followed " + username + " . \n")
    main()

def delete_favs():
    apii = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    favs = tweepy.Cursor(apii.favorites).items()
    for fav in favs:
        apii.destroy_favorite(fav.id)
        time.sleep(1)
    print("All favourites have been deleted. \n")
    main()

def unfollow(username):
    apii = login(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    apii.destroy_friendship(username)
    print("Successfully unfollowed " + username + " . \n")
    main()

def main():
    print("Type 'tweet' to send tweet.")
    print("Type 'delete_tweets' to delete your tweets.")
    print("Type 'follow' to follow someone.")
    print("Type 'unfollow' to unfollow someone.")
    print("Type 'delete_favs' to delete your favourites.")
    print("Type 'exit' to exit from script.")

    choice = input()
    if (choice.lower() == "tweet"):
        tweet(input("Please type your tweet : "))
    elif (choice.lower() == "delete_tweets"):
        delete_tweets()
    elif (choice.lower() == "follow"):
        follow(input("Please type username :"))
    elif (choice.lower() == "unfollow"):
        unfollow(input("Please type username :"))
    elif (choice.lower() == "delete_favs"):
        delete_favs()
    elif (choice.lower() == "exit"):
        sys.exit
    else:
        print("Please make your choice correctly.")

if __name__ == '__main__':
    main()
