from searchtweets import (gen_request_parameters,
                          load_credentials,
                          collect_results)

search_args = load_credentials(
        "../.twitter_keys.yaml",
        yaml_key="search_tweets_v2",
        env_overwrite=False)

query = gen_request_parameters("snow", results_per_call=100)

tweets = collect_results(
        query, 
        max_tweets=10,
        result_stream_args=search_args)

for tweet in tweets[0:5]:
    print(tweet['text'], end='\n\n')
