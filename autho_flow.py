import json
import requests
from secrets import clientId, clientSecret
import base64

# This function called each time the app will run forn us to a get a valid token
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    # Encode as Base64
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode('ascii')
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode('ascii')
    # Setting the header for Authorization based on the spotify docs
    headers['Authorization'] = f"Basic {base64Message}"
    
    # The token the app will be using to get the access tocken everytime we run the app
    refresh_token="AQAuhq2nHlWQIpSIXJP4R1Tr3XkjwujvoTXox6PeCTBA-RkI1_miu16YT_3lH64KAyYj-d5TESB4rYDC8RPkpaai4KmIDkb-k2VuA8rWLDBpuGNMdyeyj1pqS2SV4UZfXDk"

    # The requeste body thats is required for getting the token
    data['grant_type'] = "refresh_token"
    data['refresh_token'] = refresh_token

    r = requests.post(url, headers=headers, data=data)
    print(json.dumps(r.json(), indent=2))

    access_token= r.json()['access_token']
    return access_token



