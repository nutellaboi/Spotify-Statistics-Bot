import telegram
import configparser as cfg
from config_reader import ConfigReader
from spotify_api import *
import json

cfg=ConfigReader('config.cfg')

bot_token = cfg.read_token_from_config_file()
chat_id = cfg.read_user_id_from_config_file()

#print('Token->',token)
#print('UserId->',chat_id)

bot=telegram.Bot(token=bot_token)
#print(bot.get_me())
#print(bot.getUpdates()[-1].message.chat_id)#to get chat_id

todays_timestamp=get_todays_timestamp()
todays_songs_dict=get_my_todays_recently_played_songs(todays_timestamp)

song_list_msg=''
for key in todays_songs_dict:
    song_list_msg = song_list_msg + f'{key}' + ' : '+ f'{todays_songs_dict[key]}\n'

top_artists=get_my_top_artist(5)

top_artists_msg='Your Top 5 Artists :\n'
for i in range(len(top_artists)):
    top_artists_msg = top_artists_msg + f'{i+1}. {top_artists[i]}\n'


bot.send_message(text=f'Hey! You listned to {len(todays_songs_dict)} songs today.',chat_id=chat_id)
bot.send_message(text=song_list_msg,chat_id=chat_id)
bot.send_message(text=top_artists_msg,chat_id=chat_id)