import aiohttp
import asyncio
from io import BytesIO


__all__ = ('__version__', 'Client')
__version__ = '1.5'


class GatewayError(Exception):
    def __init__(self, message: str = 'API Returned a 502 status.'):
        super(GatewayError, self).__init__(message)


class UnauthorizedError(Exception):
    def __init__(self, message: str = 'API Returned a 403 status.'):
        super(UnauthorizedError, self).__init__(message)


class Client:
    """Client to gain functionality with the Zane API.
    You must pass in a token argument you can get this on the
    Zane API site. (https://zane.ip-bash.com/)

    Example:
    client = aiozaneapi.Client('Token Here') # Instantiate the Client.
    image = await client.magic('Image URL Here') # This will return a BytesIO object.
    """

    def __init__(self, token: str) -> None:
        headers = {
            'User-Agent': f'aiozaneapi v{__version__}',
            'Authorization': f'{token}'
        }
        self.session = aiohttp.ClientSession(
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=60.0)
        )

        self.base_url = 'https://zane.ip-bash.com'

    async def magic(self, url: str, magnitude: float = 0.6) -> BytesIO:
        """Applies a magic filter to a given image. Gif."""

        params = {
            'url': url,
            'magnitude': str(magnitude),
        }
        async with self.session.get(f'{self.base_url}/api/magic', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def floor(self, url: str) -> BytesIO:
        """Applies a floor effect to a given image. Gif."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/floor', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def deepfry(self, url: str) -> BytesIO:
        """Applies a deepfry effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/deepfry', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def dots(self, url: str) -> BytesIO:
        """Dotifies a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/dots', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def jpeg(self, url: str) -> BytesIO:
        """Applies a jpeg effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/jpeg', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def spread(self, url: str) -> BytesIO:
        """Applies a spread effect to a given image. Gif."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/spread', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def cube(self, url: str) -> BytesIO:
        """Turns a given image into a cube."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/cube', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def sort(self, url: str) -> BytesIO:
        """Applies a sort effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/sort', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def palette(self, url: str) -> BytesIO:
        """Gives a colour palette of a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/palette', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def invert(self, url: str) -> BytesIO:
        """Applies an invert effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/invert', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def posterize(self, url: str) -> BytesIO:
        """Applies a posterize effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/posterize', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def grayscale(self, url: str) -> BytesIO:
        """Applies a grayscale effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/grayscale', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    greyscale = grayscale

    async def pixelate(self, url: str, scale: float = 0.3) -> BytesIO:
        """Applies a pixelate effect to a given image."""

        params = {
            'url': url,
            'scale': str(scale),
        }
        async with self.session.get(f'{self.base_url}/api/pixelate', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def swirl(self, url: str, angle: int = 280) -> BytesIO:
        """Applies a swirl effect to a given image. Gif."""

        params = {
            'url': url,
            'angle': str(angle),
        }
        async with self.session.get(f'{self.base_url}/api/swirl', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def sobel(self, url: str) -> BytesIO:
        """Applies a sobel effect to a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/sobel', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.read()

        buffer = BytesIO(data)
        return buffer

    async def braille(self, url: str) -> str:
        """Returns a braille version of a given image."""

        params = {'url': url}
        async with self.session.get(f'{self.base_url}/api/braille', params=params) as resp:
            if resp.status == 502:
                raise GatewayError()
            if resp.status == 403:
                raise UnauthorizedError()

            data = await resp.text()

        return data

    async def close(self) -> None:
        """Closes the Client."""

        return await self.session.close()
