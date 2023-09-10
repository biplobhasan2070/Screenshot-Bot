import os
from pathlib import Path

class Config:
    
    API_ID = int("5310709")
    API_HASH = "63a546bdaf18e2cbba99f87b4274fa05"
    BOT_TOKEN = "5462641835:AAHBBA7u2XTcqP1uusarSxDAHhXCjH1Z940"
    SESSION_NAME = "NFS BOT"
    LOG_CHANNEL = int("-1001689617681")
    DATABASE_URL = "mongodb+srv://nfs:nfs@cluster0.ose63hs.mongodb.net/?retryWrites=true&w=majority"
    AUTH_USERS = int("1226270709")
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 2))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 600))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', False))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 15))
    HOST = os.environ.get('HOST', '')
    
    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
