from setuptools import find_packages, setup

setup(
    name="domain_project",
    packages=find_packages(exclude=["domain_project_tests"]),
    install_requires=[
        "dagster",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
