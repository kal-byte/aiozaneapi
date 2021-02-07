aiozaneapi - An async wrapper made in Python for Zane API.
==========================================================

Made for Python 3.6+.
`Website Link <https://zaneapi.com/>`_

Example:
--------

.. code:: py

    import aiozaneapi # Import the package so it can be used.

    client = aiozaneapi.Client('Token Here') # Instantiate the Client.

    try:
        image = await client.magic('Image URL Here') # This will return a BytesIO object.
    except aiozaneapi.GatewayError as err:
        print(f'Error has occurred on the server-side. {err}')
    except aiozaneapi.UnauthorizedError as err:
        print(f'Error has occurred on the client-side. {err}')

    await client.close() # Close the client unless you want aiohttp screaming at you.
