from setuptools import setup

setup(
    name='autofw',
    version='5.0.3',
    description='Pytest plugin',
    author="krunal",
    author_email="krunalprajapati1904@gmail.com",
    # packages=['autofw', 'autofw.fixture_plugin'],
    install_requires=['pytest', 'selenium'],
    entry_points={"pytest11": ["plugin1 = autofw.fixture_plugin.a","plugin2 = autofw.simple_plugin.b"]},
    url="https://github.com/krunal1904/autofw-package.git",
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Framework :: Pytest"
    ],
)

