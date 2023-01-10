import praw

def reddit():
    post = []
    titles = []
    reddit = praw.Reddit(client_id = ' ', 
    client_secret = ' ', 
    username = ' ', 
    password = ' , 
    user_agent = ' ')

    subreddit = reddit.subreddit('AskReddit')

    hot = subreddit.hot(limit = 2)
    for x in hot:
        title = x.title
        titles.append(title)
        comments = x.comments[:2]
        for comment in comments:
            com = comment.body
            post.append(com)
    return titles,post
