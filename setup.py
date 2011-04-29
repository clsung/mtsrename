try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MTS Rename',
    'author': 'Cheng-Lung Sung',
    'url': '',
    'download_url': '',
    'author_email': 'clsung@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mtsrename'],
    'scripts': [],
    'name': 'mtsrename'
}

setup(**config)
