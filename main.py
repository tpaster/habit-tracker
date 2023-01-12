import requests
from datetime import datetime

USERNAME = "MY_USERNAME"
TOKEN = "MY_TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Yoga Graph",
    "unit": "Times Per Day",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you do yoga today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "60"
}

## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
