from setuptools import setup, find_packages

setup(
    name="cwh-py",
    packages=find_packages(where="cwh-py"),  # Look for packages inside cwh-py directory
    package_dir={"": "cwh-py"},  # Tell setuptools where to find the packages
    version="0.1.0",
)
