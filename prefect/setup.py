from setuptools import setup

setup(
    name='piplines',
    version='0.1.0',
    py_modules=['piplines'],
    install_requires=[
        'Click', 'prefect', 'pandas',
    ],
    entry_points={
        'console_scripts': [
            'piplines = piplines:start_pipline',
        ],
    },
)