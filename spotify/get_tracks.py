import os
import requests
import re
from dotenv import load_dotenv

load_dotenv("spotify/spotify.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

def get_access_token():
    """Get a fresh access token using the refresh token.

    Raises:
        Exception: Unable to get an access token

    Returns:
        JSON Object: our fresh access token
    """
    token_url = "https://accounts.spotify.com/api/token"
    auth_header = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }

    response = requests.post(token_url, data=payload, auth=auth_header)

    if response.status_code != 200:
        raise Exception(f"Token refresh failed: {response.status_code} {response.text}")

    return response.json()["access_token"]

def get_top_tracks(token, limit=50):
    """Get the top played tracks from Spotify using the /top/track endpoint.

    Args:
        token (string): Spotify access token
        limit (int, optional): How many top tracks we want, default to a max of 50

    Raises:
        Exception: If API fails

    Returns:
        JSON Object: JSON containing info on a specified number of top tracks
    """
    # time_range is short_term, which is about a month
    # essentially ranked the frequencies of songs played over a month
    endpoint = f"https://api.spotify.com/v1/me/top/tracks?limit={limit}&time_range=short_term"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(endpoint, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Get Top Tracks API request failed: {response.status_code} {response.text}")

    return response.json()["items"]

def get_song_info():
    """Returns the song info for the top played song.

    Raises:
        Exception: Unable to get embed url

    Returns:
        info: dict containing relevant info
    """
    access_token = get_access_token()
    tracks = get_top_tracks(access_token, limit=1)
    track_id = ""
    info = {}
    for track in tracks:
        name = track["name"]
        album_cover = track["album"]["images"][0]["url"]
        artists = ", ".join([artist["name"] for artist in track["artists"]])
        track_id = track["id"]
        embed_url = f"https://open.spotify.com/embed/track/{track_id}"
        
        info["name"] = re.sub('[^A-z0-9 .,!?@#$%^&*()_+=:;\'\"\\[\\]{}|\\\\/<>~-]', '', name).replace("  ", " ")
        info["album_cover"] = album_cover
        info["artists"] = re.sub('[^A-z0-9 .,!?@#$%^&*()_+=:;\'\"\\[\\]{}|\\\\/<>~-]', '', artists).replace("", "")
        info["embed_url"] = embed_url
    
    if info:
        return info
    else:
        raise Exception(f"Unable to gather information on {tracks}.") 
        
print(get_song_info())
