"""Making HTTP requests with bearer token."""
import requests


def demo_fetch(url):
    """Demo_fetch function to make http request in python.

    Args:
        url (str): returns data
    """
    data = {"id": 1, "name": "bobby hadz"}
    headers = {
        "Authorization": "Bearer YOUR_JWT_TOKEN",
    }

    response = requests.post(url, data=data, headers=headers, timeout=10)
    print(response.status_code)  # 201 data created
    result = response.json()
    print(result)
    res = requests.get(url, timeout=10)
    print(res.status_code)


# demo_fetch("https://jsonplaceholder.typicode.com/users")


def demo_post(url):
    """This method for POST data."""

    res = requests.post(url, data={"key": "value"}, timeout=5)
    print(res)
    print(res.json())


demo_post("https://httpbin.org/put")
