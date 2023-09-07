"""This python file for exception handling."""
import requests


def fetch_data(url):
    """This method for successful connection.

    Args:
        url (str):Return response ok.
    """

    response = requests.get(url, timeout=5)
    print(response.status_code)


# fetch_data("https://httpbin.org")


def fetch(url):
    """This method for raise HTTPerror.

    Args:
        url (str):return data.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("HTTP error")
    print(response)


# fetch("https://api.publicapis.org/entries1")


def fetch_info(url):
    """This method for general exception handling.

    Args:
        url (str): Return data.
    """
    try:
        data = requests.get(url, timeout=5)
        data.raise_for_status()
    except requests.exceptions.RequestException:
        print("Exception raised")


# fetch_info("https://google.com")


def fetch_ms(url):
    """his method for handling MissingSchema.

    Args:
        url (str): _description_
    """
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
    except requests.exceptions.MissingSchema:
        print("MissingSchema with http or https")


# fetch_ms("www.google.com")


def fetch_conn(url):
    """This method for handling connection error
    when there is no internet connection.

    Args:
        url (str): _description_
    """
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("Connection error")


fetch_conn("https://api.publicapis.org/entries")
