from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file_obj: 
        requirements=file_obj.readlines() #Reaad the lines from the file object to get the list of requirements
        requirements = [req.replace("\n", " ")for req in requirements] #To remove the next line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements






setup(
    name = 'mlproject',
    version='1.0.0',
    author='Sankrita Patel',
    author_email='patelsankrita6960@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)