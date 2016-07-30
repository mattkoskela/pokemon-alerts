from setuptools import setup

with open("pokemonalerts/version.py") as f:
    exec(f.read())

setup(
    name="pokemon-alerts",
    version=__version__,
    license="Apache Software License",
    author="Matt Koskela",
    author_email="mattkoskela@gmail.com",
    packages=["pokemonalerts"],
    scripts=[
        "bin/pokemon-alerts"
    ],
    url="http://www.mattkoskela.com/",
    description="This package contains a commandline script to find pokemon in Pokemon Go, based off the pokevision.com API.",
    long_description=open("README.md").read(),
    install_requires=[
        "geopy==1.11.0",
        "requests==2.10.0",
        "twilio==5.4.0"
    ]
)
