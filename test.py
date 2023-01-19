import praw
import prawcore.exceptions
from random import choice
import auth

reddit = praw.Reddit(
    client_id=auth.CLIENT_ID,
    client_secret=auth.CLIENT_SECRET,
    user_agent="Ratioer by /u/loserifybot",
    password=auth.PASSWORD,
    username=auth.USERNAME
)

subreddits = [reddit.subreddit("memes"), reddit.subreddit("shitposting"), reddit.subreddit("teenagers"),
              reddit.subreddit("196"), reddit.subreddit("dankmemes"), reddit.subreddit("danidev"),
              reddit.subreddit("copypasta"), reddit.subreddit("gonewild"), reddit.subreddit("guro")]

i = 0

repliedcomments = []

def nerdemoji(comment):
    return f"\"{comment.body}\" -🤓"

def blablabla(comment):
    if comment.subreddit != reddit.subreddit("teenagers"):
        return comment.body[:int(len(comment.body)/2)] + "... bla bla bla shut the fuck up"
    else:
        return comment.body[:int(len(comment.body) / 2)] + "... bla bla bla shut the hell up"

FUNLIST = [nerdemoji, blablabla]

def generate_response(commentbody):
    return choice(FUNLIST)(commentbody) + "\n\n^(I'm a bot and this action was performed automatically.)"

while True:
    for subreddit in subreddits:
        for comment in subreddit.comments(limit=None):
            if comment.score <= -5 and comment not in repliedcomments:
                try:
                    #comment.reply(generate_response(comment.body))
                    #repliedcomments.append(comment)
                    #print(f"commented {generate_response(comment)} on " + comment.permalink)
                    pass
                except prawcore.exceptions.Forbidden:
                    print("Forbidden to reply on " + comment.permalink)
                except Exception as e:
                    print(e)

        print("checked " + subreddit.display_name)