from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    returns: list of libraries mentioned in requirements.txt
    """
    requirements = []
    with open("requirements.txt") as requirement_file:
        requirements = requirement_file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="Credit-Card-Fraud-Detection-Using-Machine-Learning"
    version="0.0.1"
    author="Linto Sunny"
    author_email="lintosunny111@gmail.com"
    install_requires=get_requirements()
    packages=find_packages()  # this will get the local packages
)
