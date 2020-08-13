import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="feed_stream",
    version="0.0.2",
    description="A streamable version of pandas.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mwbrulhardt/feed",
    author="Matthew Brulhardt",
    author_email="mwbrulhardt@gmail.com",
    license="GPL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True
)
