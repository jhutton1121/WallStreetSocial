import pandas as pd
import datetime as dt
from pmaw import PushshiftAPI


def get_reddit_comments(subreddit, before, after):
    """Returns a dataframe containing comments from a particular subreddit between
       given date frame defined by before and after.
       Before and after variables must be converted to epoch time before calling them as arguments.
    """
    api = PushshiftAPI()
    comments = api.search_comments(subreddit=subreddit, before=before, after=after)
    comments_df = pd.DataFrame(comments)
    comments_df = clean_comments_dataframe(comments_df)
    comments_df.drop_duplicates()
    return comments_df


def clean_comments_dataframe(comments_df):
    comments_df = comments_df.drop(
        ['all_awardings', 'associated_award', 'author_flair_background_color', 'author_flair_css_class',
         'author_flair_richtext',
         'author_flair_template_id', 'author_flair_text', 'author_flair_text_color', 'author_flair_type',
         'author_fullname', 'author_patreon_flair', 'author_premium', 'awarders', 'collapsed_because_crowd_control',
         'comment_type', 'gildings', 'is_submitter', 'locked', 'no_follow', 'send_replies', 'top_awarded_type',
         'treatment_tags', 'author_cakeday', 'distinguished'], axis=1)
    return comments_df


before = int(dt.datetime(2021, 1, 2, 12, 0).timestamp())
after = int(dt.datetime(2021, 1, 2, 11, 0).timestamp())

comments = get_reddit_comments('wallstreetbets', before, after)
comments.head()