from setuptools import setup

setup(
    name='check_library',
    version='1.0.4',
    author='Bapth',
    description='Check and update libraries in a requirements file ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Bapth-R/check_library.git',
    py_modules=['check_library'],
    license = 'Apache License, Version 2.0',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'check_library=check_library:main',
        ],
    },
)
