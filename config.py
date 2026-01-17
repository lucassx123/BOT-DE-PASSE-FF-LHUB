import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
LHUB_API_KEY = os.getenv("LHUB_API_KEY")
LHUB_API_URL = os.getenv("LHUB_API_URL", "https://passesff.squareweb.app")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

EMBED_COLOR = 0x9B59B6
SUCCESS_COLOR = 0x2ECC71
ERROR_COLOR = 0xE74C3C
WARNING_COLOR = 0xF39C12

PRICES = {
    "passe": 4.00,
    "likes": 1.00,
    "guest": 5.00,
    "bypass": 10.00
}
