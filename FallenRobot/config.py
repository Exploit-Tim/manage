class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 26544005
    API_HASH = "66f6221e5ce9109827b50eaf3d105025"

    CASH_API_KEY = "2G27FIONSHYJ22SK"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://postgres.jocwxwsjzbhzevpifnnl:KontolXD#123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002535004474)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://wtfbruh:KontolXD#123@fsub.brzgete.mongodb.net/?retryWrites=true&w=majority&appName=fsub"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://files.catbox.moe/88u4eu.jpg"

    SUPPORT_CHAT = "reymalvinn"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7825113154:AAFZC9KanolVQWm8zSOOYqxhb9Yf5gJKPhk"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "7VR1D5XRDTZ5"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6904648429  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [5870285414]  # List of groups that you want blacklisted.
    DRAGONS = [5870285414]  # User id of sudo users
    DEV_USERS = [5870285414]  # User id of dev users
    DEMONS = [5870285414]  # User id of support users
    TIGERS = [5870285414]  # User id of tiger users
    WOLVES = [5870285414]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
