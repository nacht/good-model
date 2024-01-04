import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "good-model",
    version = "0.0.1",
    author = "C Le-Huy",
    author_email = "cat@goodengine.xyz",
    description = ("Shared database model between Good Engine projects"),
    license = "Proprietary",
    keywords = "example documentation tutorial",
    url = "https://github.com/nacht/good-model",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Other/Proprietary License",
    ],
)
