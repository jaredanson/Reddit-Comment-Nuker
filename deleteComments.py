import praw

r = praw.Reddit(user_agent='deletingComments')
# Enter your real username and password before running the python script.
yourUserName = 'username'
yourPassword = 'password'

r.login(yourUserName, yourPassword)

# This will allow you to grab up to 1k comments at a time.
setLimit = None

user = r.get_redditor(yourUserName)

userComments = user.get_comments(limit=setLimit)

# The only way to truely "delete" your comments is to edit the original contents.
# Since reddit stores even deleted comments.

for comment in userComments:
    comment.edit('The Sky is Blue.')
