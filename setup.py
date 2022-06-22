import setuptools
from setuptools import find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fincher",
    version="0.0.1",
    author="AnimoSolus",
    author_email="animosolus@gmail.com",
    description="Library for backtesting markets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/animosolus/fincher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    packages=["pandas", "numpy"],
)
