import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7951305676:AAFExtyFSrU_Ao9E7DWj9m6geEyO9CFcoXk")
    API_ID = int(os.environ.get("API_ID",'21567814' ))
    API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
    
    
