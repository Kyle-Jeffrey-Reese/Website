import praw
import jp_regex
import requests

kanji = r'[㐀-䶵一-鿋豈-頻]'
reddit = praw.Reddit(
    user_agent="Comment Extraction (by u/USERNAME)",
    client_id="MgscZwplj5P1NEbU9pjRgw",
    client_secret="iaRaCR07fvTgSYQ1e1ycrBLRqZ7tdg"#,
    #username="USERNAME",
    #password="PASSWORD",
)

learnjapanese_kanji_frequency = {}
newsokur_kanji_frequency = {}


def pulling_reddit_japanese_text(subreddit, character_type, dictionary):
    '''From reddit, pull all of a certain type of Japanese text 
       and store in a dictionary'''
    
    for comment in reddit.subreddit(subreddit).comments(limit=None):
        subreddit_characters = jp_regex.extract_unicode_block(character_type, comment.body)
        print(subreddit_characters)
        for characters in subreddit_characters:
            if characters in dictionary:      #create text counter or add one to text already existing
                dictionary[characters] += 1
            else:
                dictionary[characters] = 1


pulling_reddit_japanese_text('learnjapanese', kanji, learnjapanese_kanji_frequency)
pulling_reddit_japanese_text('newsokur', kanji, newsokur_kanji_frequency)



def get_pushshift_data(data_type, **kwargs):
    """
    Gets data from the pushshift api.
 
    data_type can be 'comment' or 'submission'
    The rest of the args are interpreted as payload.
 
    Read more: https://github.com/pushshift/api
    """
 
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    return request.json()

data_type="comment"     # give me comments, use "submission" to publish something
query="python"          # Add your query
duration="30d"          # Select the timeframe. Epoch value or Integer + "s,m,h,d" (i.e. "second", "minute", "hour", "day")
size=200                # maximum 1000 comments
sort_type="score"       # Sort by score (Accepted: "score", "num_comments", "created_utc")
sort="desc"             # sort descending
aggs="subreddit"        #"author", "link_id", "created_utc", "subreddit"
subreddit = 'learnjapanese'
fields = 'body'
data = get_pushshift_data(data_type=data_type,
                          after=duration,
                          size=size,
                          subreddit=subreddit,
                          fields=fields)













