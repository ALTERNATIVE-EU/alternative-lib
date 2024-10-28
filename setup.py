from setuptools import find_packages, setup

setup(
    name='alternative-eu-lib',
    packages=find_packages(include=['alternative_lib']),
    version='0.2.1',
    description='Python library for working with the Alternative platform.',
    author='ALTERNATIVE',
    license='MIT',
    install_requires=['ckanapi==4.7.0'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
