from setuptools import setup, find_packages

setup(
    name="pylitsearch",
    version="0.1.0",
    description="A tool for systematic literature search using Google Scholar",
    author="ShinjiEto",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0",
        "scholarly>=1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "pylitsearch=pylitsearch.app:run"
        ]
    }
)
