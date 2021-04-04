import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime
from datetime import timedelta
from config_reader import ConfigReader
import json

cfg=ConfigReader('config.cfg')

client_id=cfg.read_client_id_from_config_file()
client_secret=cfg.read_client_secret_from_config_file()
scope=cfg.read_scope_from_config_file()
username=cfg.read_username_from_config_file()

class DateTimeFormatting:

    def __init__(self):
        pass

    def convert_string_to_datetime_ist(self,time_string):
        datetime_obj_utc=datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S.%fZ')#UTC format
        datetime_obj_ist=datetime_obj_utc+timedelta(hours=5,minutes=30)
        return datetime_obj_ist

    def convert_datetime_to_suitable_format(self,date):#dd-mm-yyyy h:m:s
        suitable_format=date.strftime('%d-%m-%Y %H:%M:%S')
        return suitable_format

    def get_todays_timestamp(self):#get todays timestamp with 00:00:00
        todays_timestamp=datetime.now()#exact time
        todays_timestamp_str=f'{todays_timestamp.day}-{todays_timestamp.month}-{todays_timestamp.year} 00:00:00'
        todays_timestamp_zero_hms=datetime.strptime(todays_timestamp_str, '%d-%m-%Y %H:%M:%S')
        return todays_timestamp_zero_hms.timestamp()

dtf_obj=DateTimeFormatting()
todays_timestamp=dtf_obj.get_todays_timestamp()
print(todays_timestamp)

def get_token(client_id,client_secret,scope,username):
    token=spotipy.util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri='http://localhost:8080/callback')
    return token

def get_my_todays_recently_played_songs(today_timestamp):
    todays_history = sp.current_user_recently_played(limit=50,after=None,before=None)
    #with open('data.txt', 'w') as outfile:
    #   json.dump(todays_history, outfile)
    todays_songs_dict={}
    for i in range(len(todays_history['items'])):
        track_name=todays_history['items'][i]['track']['name']
        #artist_name=todays_history['items'][i]['track']['artists'][0]['name']
        played_date_time_dateformat=dtf_obj.convert_string_to_datetime_ist(todays_history['items'][i]['played_at'])
        played_date_time_timestamp=played_date_time_dateformat.timestamp()
        if(played_date_time_timestamp >= today_timestamp):    
            todays_songs_dict.update({f'{track_name}':dtf_obj.convert_datetime_to_suitable_format(played_date_time_dateformat)})
    return todays_songs_dict

def get_my_top_artist(number=1):
    user_top_artists = sp.current_user_top_artists(limit=number,offset=0,time_range="short_term")
    top_artist_list=[]
    for i in range(len(user_top_artists['items'])):
        top_artist_list.insert(i, user_top_artists['items'][i]['name'])
    return top_artist_list

def get_my_currently_playing_song():
    currently_playing=sp.current_user_playing_track()
    return currently_playing['item']['name']


auth_token=get_token(client_id, client_secret, scope, username)
sp = spotipy.Spotify(auth=auth_token)

todays_timestamp=dtf_obj.get_todays_timestamp()
todays_songs_dict=get_my_todays_recently_played_songs(todays_timestamp)

print(f'{todays_songs_dict} : {len(todays_songs_dict)}')
print(f'My Top 5 Artist is {get_my_top_artist(5)}')
#print(f'Currently playing : {get_my_currently_playing_song()}')

