from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="calclib",
    version="0.1.0",
    author="Vickey",
    author_email="vv6250625@gmail.com",
    description="A simple calculator library for basic arithmetic operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vickey-vijay/calclib/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
