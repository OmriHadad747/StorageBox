import os

from api.app import createApp


app = createApp(os.getenv("FLASK_ENV"))