import os
from dotenv import load_dotenv

load_dotenv()

try:
    API_ID = int(os.environ.get('API_ID', 0))
except ValueError:
    raise Exception("Your API_ID is not a valid integer.")
API_HASH = os.environ.get('API_HASH', None)
print(API_HASH)
BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
DATABASE_URL = os.environ.get('DATABASE_URL', None)
MUST_JOIN = os.environ.get('MUST_JOIN', None)
if MUST_JOIN.startswith("@"):
    MUST_JOIN = MUST_JOIN.replace("@", "")
INSTA_USERNAME = os.environ.get('INSTA_USERNAME', None)
INSTA_PASSWORD = os.environ.get('INSTA_PASSWORD', None)