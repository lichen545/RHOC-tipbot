import praw


class Listener:
    def __init__(self, reddit, subreddit, log):
        self.reddit = reddit
        self.subreddit = subreddit
        self.log = log

    def find_references(self):
        while True:
            subreddit = self.reddit.subreddit(self.subreddit)

            self.log.info('Scraping r/' + self.subreddit + '...')

            try:
                for comment in subreddit.stream.comments():
                    command = ['!tiprhoc']
