from setuptools import find_packages, setup

setup(  
    name='mylibrary',
    packages=find_packages(include='mylibrary'),
    version= '0.0.1',
    description='My python library',
    author= 'Tor',
    license='MIT',
    install_requires= [],
    setup_requires=['pytst-runner'],
    tests_requires=['pytest==4.4.1'],
    test_suite='tests',
)