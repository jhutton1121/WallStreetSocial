import json
import datetime as dt
from pmaw import PushshiftAPI
from multiprocessing import cpu_count

class Reddit:
    def __init__(self, subreddit, before, after, num_workers) -> None:
        self.subreddit = subreddit
        self.before = before
        self.after = after
        self.num_workers = num_workers

    def get_reddit_comments(self):
        """Returns a list containing comments from a particular subreddit between
        given date frame defined by before and after.
        Before and after variables must be converted to epoch time before calling them as arguments.
        """
        api = PushshiftAPI()
        comments = api.search_comments(
            subreddit = self.subreddit,
            before = self.before,
            after = self.after,
            num_workers = self.num_workers
        )
        return [comment for comment in comments]

    def _comment_seed(self, comment_list):
        seed = []
        for i, comment in enumerate(comment_list):
            seed.append(
                {
                    "model": "raw_reddit_comments.RawComment",
                    "pk": i,
                    "fields": {
                        "comment_id": comment.get('id'),
                        "comment_timestamp": comment.get('created_utc'),
                        "comment_body": comment.get('body'),
                        "comment_upvotes": comment.get('score')
                    }
                }
            )
        return seed

    def get_reddit_backfill(self):
        comments = self.get_reddit_comments()
        seed = self._comment_seed(comments)
        with open('comment_seed.jsonl', 'w') as outfile:
            for entry in seed:
                json.dump(entry, outfile)
                outfile.write('\n')

subreddit = 'wallstreetbets'
before = int(dt.datetime(2021, 1, 2, 12, 0).timestamp())
after = int(dt.datetime(2021, 1, 2, 11, 0).timestamp())
num_workers = cpu_count() - 1



    


if __name__ == "__main__":
    Reddit(subreddit, before, after, num_workers).get_reddit_backfill()