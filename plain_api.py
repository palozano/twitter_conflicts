import requests
import os
import json
import yaml

with open('../.twitter_keys.yaml') as file:
    document = yaml.full_load(file)
    bearer_token = document['search_tweets_v2']['bearer_token']

search_url = "https://api.twitter.com/2/tweets/search/all"

query_params = {
        # 'query':        '(from:twitterdev -is:retweet) OR #twitterdev',
        'query':        '(from:twitterdev)',
        'tweet.fields': 'author_id'
        }


def create_url():
    query = "from:twitterdev -is:retweet"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, start_time,end_time,since_id,until_id,max_results,next_token, expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fieldsauthor_id, context_annotations, conversation_id, created_at, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, source, text, and withheld
    tweet_fields = "tweet.fields=author_id"

    # all_url = "https://api.twitter.com/2/tweets/search/all"
    recent_url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )

    return recent_url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", search_url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(search_url, headers, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
