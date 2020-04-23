# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
# from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import twitter_api_client
# from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
def get_user(screen_name=None):
    print(screen_name)

    api = twitter_api_client()

    twitter_user = api.get_user(screen_name)
    statuses = api.user_timeline(screen_name, tweet_mode="extended", count=150, exclude_replies=True, include_rts=False)
    print("STATUSES COUNT:", len(statuses))
    return jsonify({"user": twitter_user._json, "tweets_count": len(statuses)})

    # get existing user from the db or initialize a new one:
    # db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    # db_user.screen_name = twitter_user.screen_name
    # db_user.name = twitter_user.name
    # db_user.location = twitter_user.location
    # db_user.followers_count = twitter_user.followers_count
    # db.session.add(db_user)
    # db.session.commit()
    #breakpoint()
    return "OK"
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets



    