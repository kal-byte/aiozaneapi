from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='aiozaneapi',
    version='1.3',
    description='An async wrapper made in Python for Zane API.',
    long_description=long_description,
    url='http://github.com/kal-byte/aiozaneapi',
    author='kal-byte',
    license='MIT',
    packages=['aiozaneapi'],
    install_requires=['aiohttp'],
    requirements=requirements,
    zip_safe=False,
)
