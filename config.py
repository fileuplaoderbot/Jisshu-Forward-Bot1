# bot developer @im_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "26683574")
    API_HASH = environ.get("API_HASH", "69ba051f43cff367bf569bd54eb277a7")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8062609271:AAHTXGUMBOIRHE-MmwOK5iwUkqZnGqS5ppw") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6069621485').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://i.supaimg.com/53fa6de8-c1c2-4c17-8ff4-d0ffd389d9eb/78e70e4c-3086-4d14-91c2-e0b517621d9a.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1004322054909'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/+KNbm-z52EvhkOGU1") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    FORWARD_TASKS = {}
    
