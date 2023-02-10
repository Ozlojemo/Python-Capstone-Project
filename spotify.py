
#Spotify API
import requests
import json
from autho_flow import get_access_token

# Used to get the access token to be used for Authorization
token= get_access_token()
headers = {"Authorization": "Bearer " + token}

# Getting the playlist info
USA_playlist_id = "37i9dQZEVXbLp5XoPON0wI"
global_playlist_id = "37i9dQZEVXbMDoHDwVN2tF"
global_top_50_playlist = f"https://api.spotify.com/v1/playlists/{global_playlist_id}/tracks?limit=5"
USA_top_50_playlist = f"https://api.spotify.com/v1/playlists/{USA_playlist_id}/tracks?limit=5"
global_response = requests.get(url=global_top_50_playlist, headers=headers)
USA_response = requests.get(url=USA_top_50_playlist, headers=headers)

# The list that will store track ids from the playlists
my_track_ids = []

# Loop through the track list and add the song Ids to the my_track_ids list
global_response_json = global_response.json()
my_global_tracks_list = global_response_json["items"]
for track in my_global_tracks_list:
    track_info_id = track["track"]["id"]
    my_track_ids.append(track_info_id)

USA_response_json = USA_response.json()
my_USA_tracks_list = USA_response_json["items"]
for track in my_USA_tracks_list:
    track_info_id = track["track"]["id"]
    my_track_ids.append(track_info_id)

# The string of the track uris
list_of_track_uris = ""
# Loop through the track Ids and use them to create track uris
for track_id in my_track_ids:
    list_of_track_uris = list_of_track_uris + f"spotify%3Atrack%3A{track_id}%2C"

# Adding the tracks to the play list
playlist_id = "2a765mFBKp3GYoC3F5cSMn"
posts_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={list_of_track_uris}"
save_track_response = requests.post(url=posts_url, headers=headers)