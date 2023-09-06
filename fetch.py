"""Python file to use of requests module."""
import requests


def fetch(url):
    """Fetch method to fetch data and print key value."""
    res = requests.get(url, timeout=3)
    res1 = res.json()
    print(res1["authorizations_url"])
    print(res.headers)
    print(f"parsing the headers,{res.headers['Date']}")


# fetch(url="https://api.github.com")


def fetch_data(url):
    """This method to fetch data with key.

    Args:
        url (str): returns data.
    """
    query_ = {"input": "new york", "limit": "10"}
    headers = {
        "X-RapidAPI-Key": "a9904a0453mshd2c9009ad69b5a2p1034bejsnc39d1cfd16a4",
        "X-RapidAPI-Host": "realtor.p.rapidapi.com",
    }
    response = requests.get(url, timeout=2, headers=headers, params=query_)
    print(response.json())


# fetch_data(url=" "https://realtor.p.rapidapi.com/locations/v2/auto-complete"")


def fetch_post(url):
    """This is POST method for user registartion api.

    Args:
        url (str): returns invalid token data.
    """

    headers = {
        "name": "Developer",
        "email": "Developer5@gmail.com",
        "location": "USA",
        "token": "02b869e4-ea45-4b5c-b764-642a39e95bb7",
    }

    response = requests.post(url, headers=headers, timeout=4)
    print(response.json())


fetch_post("http://restapi.adequateshop.com/api/users")
