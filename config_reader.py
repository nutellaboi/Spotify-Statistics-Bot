import configparser as cfg

class ConfigReader:
    
    def __init__(self,config):
        self.config=config

    def read_client_id_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('SpotifyCreds','client_id')
    
    def read_client_secret_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('SpotifyCreds','client_secret')

    def read_username_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('SpotifyCreds','username')

    def read_scope_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('SpotifyCreds','scope')
    
    def read_token_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('BotCreds','token')   

    def read_user_id_from_config_file(self):
        parser=cfg.ConfigParser()
        parser.read(self.config)
        return parser.get('BotCreds','user_id')
