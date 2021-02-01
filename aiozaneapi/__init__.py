import aiohttp
import asyncio
from io import BytesIO


__all__ = ('__version__', 'Client')
__version__ = '1.2'


class Client:
    """Client to gain functionality with the Zane API.
    You must pass in a token argument you can get this on the
    Zane API site.

    Example:
    client = aiozaneapi.Client('Token Here') # Instantiate the Client.
    image = await client.magic('Image URL Here') # This will return a BytesIO object.
    """

    def __init__(self, token: str) -> None:
        headers = {
            'User-Agent': f'aiozaneapi v{__version__}',
            'Authorization': f'{token}'
        }
        self.session = aiohttp.ClientSession(headers=headers)

        self.base_url = 'https://zane.ip-bash.com'

    async def magic(self, url: str) -> BytesIO:
        """Applies a magic filter to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/magic', params=params) as resp:
            data = await resp.read()
        
        buffer = BytesIO(data)
        return buffer

    async def floor(self, url: str) -> BytesIO:
        """Applies a floor effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/floor', params=params) as resp:
            data = await resp.read()
        
        buffer = BytesIO(data)
        return buffer

    async def deepfry(self, url: str) -> BytesIO:
        """Applies a deepfry effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/deepfry', params=params) as resp:
            data = await resp.read()
        
        buffer = BytesIO(data)
        return buffer

    async def braille(self, url: str) -> str:
        """Returns a braille version of a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/braille', params=params) as resp:
            data = await resp.text()

        return data

    async def colour_ascii(self, url: str) -> str:
        """Returns a colour ascii version of a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/color_ascii', params=params) as resp:
            data = await resp.text()

        return data

    color_ascii = colour_ascii

    async def close(self) -> None:
        """Closes the Client."""

        return await self.session.close()