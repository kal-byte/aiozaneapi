aiozaneapi - An async wrapper made in Python for Zane API.

Made for Python 3.6+.

Example:
.. code:: py

    import aiozaneapi # Import aiozaneapi

    client = aiozaneapi.Client('Token Here') # Instantiate the Client.
    image = await client.magic('Image URL Here') # This will return a BytesIO object.
