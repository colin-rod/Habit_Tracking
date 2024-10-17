import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "vosjn4j4nfuvr9"
USERNAME = "corod"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response=requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)


graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response= requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

graph_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8"
}

#
# response= requests.post(url=graph_update_endpoint,json=graph_update_config,headers=headers)
# print(response.text)

update_date = 20241017

graph_change_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}"

graph_change_config = {
    "date": update_date,
    "quantity": "3"
}

#
# response= requests.put(url=graph_change_endpoint,json=graph_change_config,headers=headers)
# print(response.text)

graph_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}"

response = requests.delete(url=graph_delete_endpoint, headers=headers)
print(response.text)
