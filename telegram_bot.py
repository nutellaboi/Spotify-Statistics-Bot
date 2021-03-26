import telegram
import configparser as cfg
import json

def read_token_from_config_file(config):
    parser=cfg.ConfigParser()
    parser.read(config)
    return parser.get('BotCreds','token')

def read_user_id_from_config_file(config):
    parser=cfg.ConfigParser()
    parser.read(config)
    return parser.get('UserCreds','user')

token = read_token_from_config_file('config.cfg')
chat_id = read_user_id_from_config_file('config.cfg')

#print('Token->',token)
#print('UserId->',chat_id)

bot=telegram.Bot(token=token)
#print(bot.get_me())
print(bot.getChat(chat_id))
updates=bot.getUpdates()
print(updates)
#bot.send_message(text='lol',chat_id=chat_id)