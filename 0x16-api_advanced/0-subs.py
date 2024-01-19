#!/usr/bin/python3
"""Get the number of subscribers for a subreddit."""
import requests
def number_of_subscribers(subreddit):
    """Get the number of subscribers for a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    try:
        print("URL de la requête : {}".format(url))
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Vérifiez le code de statut de la réponse

        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print("Erreur lors de la requête : {}".format(e))
        return 0
