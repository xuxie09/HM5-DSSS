from distutils.core import setup
from setuptools import find_packages


setup(
    name = "snowflake",
    version = "0.1",
    author = "xuxie09",
    author_email = "levyxie@foxmail.com",
    packages = find_packages(),
    install_requires=["numpy","turtles"],
)
