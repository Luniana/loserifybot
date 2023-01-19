import praw
import prawcore.exceptions
from random import choice
import auth

reddit = praw.Reddit(
    client_id=auth.CLIENT_ID,
    client_secret=auth.CLIENT_SECRET,
    user_agent="Ratioer by dmtrltrptmn",
    password=auth.PASSWORD,
    username=auth.USERNAME,
    ratelimit_seconds=700
)

subreddits = [reddit.subreddit("memes"), reddit.subreddit("shitposting"),
              reddit.subreddit("196"), reddit.subreddit("dankmemes"), reddit.subreddit("danidev"),
              # reddit.subreddit("copypasta"),
              reddit.subreddit("guro"),
              # reddit.subreddit("whitepeopletwitter"),
              reddit.subreddit("meme"),
              reddit.subreddit("moldymemes"), reddit.subreddit("terriblefacebookmemes"),
              reddit.subreddit("blursedimages"), reddit.subreddit("angryupvote")]

i = 0

repliedcomments = []


def nerdemoji(comment):
    return f"\"{comment.body}\" -🤓"


def blablabla(comment):
    return comment.body[:int(len(comment.body)/2)] + "... bla bla bla shut the fuck up"


FUNLIST = [nerdemoji, blablabla]


def generate_response(commentbody):
    return choice(FUNLIST)(commentbody) + "\n\n^(I'm a bot and this action was performed automatically.)"


selfbot = reddit.redditor("loserifybot")

while True:
    for subreddit in subreddits:
        for comment in subreddit.comments(limit=None):
            if comment.score <= -10 and comment not in repliedcomments and comment.author != selfbot:
                try:
                    comment.reply(generate_response(comment))
                    repliedcomments.append(comment)
                    print(f"commented on " + comment.permalink)
                except prawcore.exceptions.Forbidden:
                    print("Forbidden to reply on " + comment.permalink)
                except Exception as e:
                    print(e)
        print("checked " + subreddit.display_name)
