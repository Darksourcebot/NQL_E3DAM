import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 15986212))

    API_HASH = os.environ.get("API_HASH", "6c6ac02bc91d512401c09279f4e69837")
