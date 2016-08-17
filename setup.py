from setuptools import setup, find_packages

setup(
    name='pokeauth',
    version='0.0.1',
    url='https://github.com/thisbejim/pokeauth-python',
    description=' A helper library for developers using pokeauth.com',
    author='James Childs-Maidment',
    license='MIT',
    keywords='Pokemon, PokemonGo',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests']
)