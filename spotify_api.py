import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from config_reader import ConfigReader
from datetimeformatting_class import DateTimeFormatting
import json

#Objects
cfg=ConfigReader('config.cfg')
dtf_obj=DateTimeFormatting()

client_id=cfg.read_client_id_from_config_file()
client_secret=cfg.read_client_secret_from_config_file()
scope=cfg.read_scope_from_config_file()
username=cfg.read_username_from_config_file()

def get_token(client_id,client_secret,scope,username):
    token=spotipy.util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost:8080/callback')
    return token

def get_my_todays_recently_played_songs(today_timestamp):
    todays_history = sp.current_user_recently_played(limit=50,after=None,before=None)
    #with open('data.txt', 'w') as outfile:
    #   json.dump(todays_history, outfile)
    todays_songs_list=[]
    for i in range(len(todays_history['items'])):
        song_dict={}
        track_name=todays_history['items'][i]['track']['name']
        artist_name=todays_history['items'][i]['track']['artists'][0]['name']
        track_duration=float(todays_history['items'][i]['track']['duration_ms'])
        played_date_time_dateformat=dtf_obj.convert_string_to_datetime_ist(todays_history['items'][i]['played_at'])
        played_date_time_timestamp=played_date_time_dateformat.timestamp()
        if(played_date_time_timestamp >= today_timestamp):
            song_dict.update({'track_name':track_name})
            song_dict.update({'artist_name':artist_name})
            song_dict.update({'track_duration':track_duration})
            song_dict.update({'played_at':dtf_obj.convert_datetime_to_suitable_format(played_date_time_dateformat)})
            todays_songs_list.append(song_dict)
    return todays_songs_list

def get_my_top_artist(number=1):
    user_top_artists = sp.current_user_top_artists(limit=number,offset=0,time_range="short_term")
    top_artist_list=[]
    for i in range(len(user_top_artists['items'])):
        top_artist_list.insert(i, user_top_artists['items'][i]['name'])
    return top_artist_list

def get_my_currently_playing_song():
    currently_playing=sp.current_user_playing_track()
    return currently_playing['item']['name']

def get_my_todays_listening_hours(todays_history_list):
    duration_ms=0.0
    for i in range(len(todays_history_list)):
        duration_ms = duration_ms + todays_history_list[i]['track_duration']
    hms=dtf_obj.convert_ms_to_hms(duration_ms)
    return hms

auth_token=get_token(client_id, client_secret, scope, username)
sp = spotipy.Spotify(auth=auth_token)

#todays_timestamp=dtf_obj.get_todays_timestamp()
#todays_history_list=get_my_todays_recently_played_songs(todays_timestamp)
#print(f'{todays_history_list} : {len(todays_history_list)}')
#print(f'{get_my_todays_listening_hours(todays_history_list)}')
#print(f'My Top 5 Artist is {get_my_top_artist(5)}')
#print(f'Currently playing : {get_my_currently_playing_song()}')

