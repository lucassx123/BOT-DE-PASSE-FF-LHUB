import aiohttp
from config import LHUB_API_KEY, LHUB_API_URL

class LHubAPI:
    def __init__(self):
        self.base_url = LHUB_API_URL
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": LHUB_API_KEY
        }

    async def get_balance(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/api/v1/balance",
                headers=self.headers
            ) as response:
                return await response.json()

    async def send_passe(self, uid: str, message: str = None):
        payload = {"uid": uid}
        if message:
            payload["message"] = message
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/v1/passe",
                headers=self.headers,
                json=payload
            ) as response:
                return await response.json()

    async def send_likes(self, uid: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/v1/likes",
                headers=self.headers,
                json={"uid": uid}
            ) as response:
                return await response.json()

    async def get_guest(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/v1/guest",
                headers=self.headers
            ) as response:
                return await response.json()

    async def send_bypass(self, uid: str, days: int = 30):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/v1/bypass",
                headers=self.headers,
                json={"uid": uid, "days": days}
            ) as response:
                return await response.json()

api = LHubAPI()
