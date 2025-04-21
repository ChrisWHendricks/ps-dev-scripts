from setuptools import setup, find_packages

setup(
    name="ps-cx-dev-util",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # 'requests>=2.25.1',
    ],
    author="Chris Hendricks",
    author_email="chris.hendricks@tylertech.com",
    description="A collection of dev utility packages",
    python_requires=">=3.6",
)
