import requests
import json

#Plan:
#Step 1: Log into Spotify
#Step 2: Access playlist object
#Step 3: Output list of song names

#########

#Step 1: Log into Spotify
CLIENT_ID = "c4dce2d4927d4f31a5469567ebfd2db1"
CLIENT_SECRET = "ad09fe39ebca46de91555327f0097926"

grant_type = 'client_credentials'
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'
response = requests.post(url, data=body_params, auth = (CLIENT_ID, CLIENT_SECRET)) 

token_raw = json.loads(response.text)
token = token_raw["access_token"]

headers = {"Authorization": "Bearer {}".format(token)}


#Step 2: Access playlist object using playlist ID
endpoint_url="https://api.spotify.com/v1/playlists/0XbYfTLwM4mgj8BmfPyujy" #This is the playlist ID for my summer playlist
#Create our query, and send an HTTP GET request to the API service
query = f'{endpoint_url}'
response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization": "Bearer {}".format(token)})
json_response = response.json()
#json_response returns a dict with playlist objects outlined in Spotify's API
tracks = json_response["tracks"]
tracks = tracks["items"]


#Step 3: Output list of song names
songList = []
for i in range(len(tracks)):
    songList.append(tracks[i]["track"]["name"])

for i in range(len(songList)):
    print(i, ") ", songList[i], sep = "")


"""
endpoint_url="https://api.spotify.com/v1/playlists/0XbYfTLwM4mgj8BmfPyujy" #This is the playlist ID for my summer playlist
#Create our query, and send an HTTP GET request to the API service
query = f'{endpoint_url}'
response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":"Bearer BQAaK_Gigvl1BbbjdfnU-BXfGAFjp81wUf_qp3czsbakoWxKsNEnIPEG5M7uTF_kTZdf76qk9Wlj3t1OCMBGprrEaQR5NkNrxT-w6pZ_yq8RMCvilphbFfxO-_FHUh8osi_9-D5sAdDZMWdiki_kN8xj1gmNRGAq7NBnq6m7mD2eIHVy1ot6skgTvYbWxnusoBUu6Xb8nXJTIevrqHoGcWsa3RjoG6oBRj_VAxYVZs36HRPp"})
json_response = response.json()
#json_response returns a dict with playlist objects outlined in Spotify's API
tracks = json_response["tracks"]
tracks = tracks["items"]

#Output list of song names
songList = []
for i in range(len(tracks)):
    songList.append(tracks[i]["track"]["name"])

for i in range(len(songList)):
    print(i, ") ", songList[i], sep = "")
"""
