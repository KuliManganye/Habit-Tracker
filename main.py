import requests
from datetime import date
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()
configure()

USER_NAME = os.getenv("USER_NAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create a graph
pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

# The pixela api requires parameters to be created in order to get the full version of the graph you aim to build
# Set the parameters:
graph_config = {
    "id": GRAPH_ID,
    "name": "Steps Graph KM",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}


response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Post the value to the graph
post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

# We will be keeping track of our walks therefore, use the datetime module to assign today's date to the program for
# every day
today_date = date.today()
today = today_date.strftime("%Y%m%d")
print(today)


# Post your daily kilometre count to the graph:
post_config = {
    "date": today,
    "quantity": input("How many kilometres did you walk today? "),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)


# Code for updating your pixela:
update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

update_config = {
    "quantity": input("How many kilometres did you walk today? "),
}

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

# Code for deleting a pixel:
"""delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)"""