import requests
import os
import json
import yaml

def load_keys():
    with open('../.twitter_keys.yaml') as file:
        document = yaml.full_load(file)
        bearer_token = document['search_tweets_v2']['bearer_token']
    return bearer_token


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# URLs
#
# Followers look-up
def url_params_followers(user_id=865577763679252480):
    url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
    params = {
            'user.fields': 'created_at'
            }
    return url, params

# Full archive search
def url_params_full_archive():
    url = "https://api.twitter.com/2/tweets/search/all"
    params = {
            'query': '(from:twitterdev -is:retweet) OR #twitterdev', 
            'tweet.fields': 'author_id'
            }
    return url, params

# Recent search
def url_params_recent():
    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
            'query': '(from:twitterdev -is:retweet) OR #twitterdev', 
            'tweet.fields': 'author_id'
            }
    return url, params

# Tweet look-up
def url_params_regular():
    url = "https://api.twitter.com/2/tweets"
    params = {
            'ids': '1278747501642657792,1255542774432063488', 
            'tweet.fields': 'lang,author_id'
            }
    return url, params

# User look-up
def url_params_user():
    url = "https://api.twitter.com/2/users/by"
    params = {
            'usernames': 'TwitterDev,TwitterAPI', 
            'user.fields': 'description,created_at'
            }
    return url, params


def main():
    bearer_token = load_keys()
    headers = create_headers(bearer_token)

    ### Uncomment one
    # search_url, query_params = url_params_followers()
    # search_url, query_params = url_params_full_archive()
    # search_url, query_params = url_params_recent()
    search_url, query_params = url_params_regular()
    # search_url, query_params = url_params_user()

    json_response = connect_to_endpoint(search_url, headers, query_params)

    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
