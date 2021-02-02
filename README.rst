aiozaneapi - An async wrapper made in Python for Zane API.

Made for Python 3.6+.

Example:
.. code-block:: python
    :linenos:
    client = aiozaneapi.Client('Token Here') # Instantiate the Client.
    image = await client.magic('Image URL Here') # This will return a BytesIO object.