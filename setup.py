import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [

]

setup(
    name='raml-parsers-test-py',
    version='0.0.1',
    description='Test few RAML Python parsers',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ],
    url='https://github.com/postatum/raml-parsers-test-py',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points="""\
    [console_scripts]
        raml-test-py = parsers_test:main
    """
)
