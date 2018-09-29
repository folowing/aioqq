from setuptools import setup, find_packages


setup(
    name='aioqq',
    version='0.1',
    description='Asyncio-based client for Tencent QQ Platform',
    author='Rocky Feng',
    author_email='folowing@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['aiohttp>=3.0.0'],
    zip_safe=False,
)
