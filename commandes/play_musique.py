import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import webbrowser
import spotipy



def musique_spotify(search_song):
    load_dotenv() 

    username =  os.getenv("username")
    client_id =  os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    redirect_url =  os.getenv("redirect_url")
    
    oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, redirect_url)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()
    
    #search_song = input("Enter the song name: ")
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results['tracks']
    song_items = songs_dict['items']
    song = song_items[0]['external_urls']['spotify']
    webbrowser.open(song)
    print('Song has opened in your browser.')



