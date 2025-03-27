import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 14681595))
    API_HASH = os.environ.get("API_HASH", "a86730aab5c59953c424abb4396d32d5")
    TOKEN = os.environ.get("TOKEN", "7725269349:AAGuTEMxnYYre1AA4BcO-_RL7N7Rz-cI3iU")
    BOT_US = os.environ.get("BOT_US", None)
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", None)
    RULES = os.environ.get("RULES", None)
