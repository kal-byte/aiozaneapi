import aiohttp
from io import BytesIO


__all__ = ('__version__', 'Client')
__version__ = '1.0'


class Client:
    """Client to gain functionality with the Zane API.
    You must pass in a token argument you can get this on the
    Zane API site.

    Example:
    client = aiozaneapi.Client('Token Here') # Instantiate the Client.
    image = await client.magik('Image URL Here') # This will return a BytesIO object.
    """

    def __init__(self, token: str) -> None:
        headers = {
            'User-Agent': 'aiozaneapi v1.0',
            'Authorization': f'{token}'
        }
        self.session = aiohttp.ClientSession(headers=headers)
        self.base_url = 'https://zane.ip-bash.com/'

    async def magik(self, url: str) -> BytesIO:
        """Applies a magik filter to a given image."""

        params = {'url': url}
        url = f'{self.base_url}api/magic'
        async with self.session.get(url, params=params) as resp:
            data = await resp.read()
        
        buffer = BytesIO(data)
        return buffer

    async def floor(self, url: str) -> BytesIO:
        """Applies a floor effect to a given image."""

        params = {'url': url}
        url = f'{self.base_url}api/floor'
        async with self.session.get(url, params=params) as resp:
            data = await resp.read()
        
        buffer = BytesIO(data)
        return buffer

    async def braille(self, url: str) -> str:
        """Returns a braille version of a given image."""

        params = {'url': url}
        url = f'{self.base_url}api/braille'
        async with self.session.get(url, params=params) as resp:
            data = await resp.text()

        return data

    async def close(self) -> None:
        """Closes the Client."""

        return await self.session.close()