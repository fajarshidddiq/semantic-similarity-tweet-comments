import subprocess
import json
import os
import pandas as pd


class TweetScraper:
    def __init__(self):
        pass

    def get_nested_value(self, data_dict, nested_key):
        keys = nested_key.split(".")
        for key in keys:
            if isinstance(data_dict, dict):
                data_dict = data_dict.get(key)
            else:
                return None
        return data_dict

    def scrape_tweet_replies(self, tweet_id: str, limit=5):
        limit = max(limit, 2)
        process = subprocess.Popen(
            ["twscrape", "tweet_replies", tweet_id, f"--limit={limit}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        if stderr:
            print(f"Error occurred: {stderr}")
            return None
        else:
            tweet_comments = stdout.strip().split("\n")
            tweet_comments_json = [
                {
                    "comment_id": comment.get("id_str"),
                    "date": comment.get("date"),
                    "rawContent": comment.get("rawContent"),
                    "tweet_id": comment.get("inReplyToTweetIdStr"),
                }
                for comment in (json.loads(c) for c in tweet_comments)
            ]
            return tweet_comments_json

    def save_replies_to_csv(self, tweet_id, replies):
        replies_csv = f"storage/replies_{tweet_id}.csv"
        if os.path.exists(replies_csv):
            replies_df = pd.read_csv(replies_csv)
        else:
            replies_df = pd.DataFrame()

        if replies:
            df_replies = pd.DataFrame(replies)
            replies_df = pd.concat([replies_df, df_replies], ignore_index=True)
        else:
            print(f"No replies found for tweet {tweet_id}")

        replies_df.to_csv(replies_csv, index=False)
        print(f"Replies saved to {replies_csv}")


def main():
    tweet_id = input("Enter tweet ID: ")
    scraper = TweetScraper()
    replies = scraper.scrape_tweet_replies(tweet_id, limit=500)
    if replies:
        scraper.save_replies_to_csv(tweet_id, replies)


if __name__ == "__main__":
    main()
