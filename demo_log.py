"""This python file for logging exception."""


import logging
import requests


logging.basicConfig(filename="error.log", level=logging.ERROR)


def fetch(url):
    """This method for handling error messages."""
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        print("Requests is successful")
    except requests.exceptions.RequestException as err:
        logging.error("Error occurred %s", err)


fetch("https://api.publicapis.org/entries")
