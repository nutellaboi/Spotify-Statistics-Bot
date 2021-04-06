import telegram
import configparser as cfg
from config_reader import ConfigReader
from datetimeformatting_class import DateTimeFormatting
from spotify_api import *
import json

#objects
cfg=ConfigReader('config.cfg')
dtf_obj=DateTimeFormatting()

bot_token = cfg.read_token_from_config_file()
chat_id = cfg.read_user_id_from_config_file()

#print('Token->',token)
#print('UserId->',chat_id)

bot=telegram.Bot(token=bot_token)
#print(bot.get_me())
#print(bot.getUpdates()[-1].message.chat_id)#to get chat_id

todays_timestamp=dtf_obj.get_todays_timestamp()
todays_songs_list=get_my_todays_recently_played_songs(todays_timestamp)

listening_hrs_msg='That is '+get_my_todays_listening_hours(todays_songs_list) +' of music in 24 hours!'

song_list_msg='These are the songs you listened to today :\n'if len(todays_songs_list)>1 else 'And that song is :\n' if len(todays_songs_list)==1 else '\"Without music, life is a journey through a desert\".\nSo start listening! '
for i in range(len(todays_songs_list)):
    song_dict=todays_songs_list[i]
    song_list_msg = song_list_msg + song_dict['track_name'] + '-' + song_dict['artist_name'] + ' : '+ song_dict['played_at']+'\n'

top_artists=get_my_top_artist(5)

top_artists_msg='Your current Top 5 Artists :\n'
for i in range(len(top_artists)):
    top_artists_msg = top_artists_msg + f'{i+1}. {top_artists[i]}\n'

#message 1
bot.send_message(text=f'Hey! You have listened to {len(todays_songs_list)} song today.'if len(todays_songs_list)==1 else 
        f'Hey! You have listened to {len(todays_songs_list)} songs today.',chat_id=chat_id)
#message 2
bot.send_message(text=listening_hrs_msg,chat_id=chat_id)
#message 3
bot.send_message(text=song_list_msg,chat_id=chat_id)
#message 4
bot.send_message(text=top_artists_msg,chat_id=chat_id)