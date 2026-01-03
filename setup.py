'''
The setup.py file is an essential part of packaging and distributing Python projects. It is used by setuptools
(or distutils in older Python versions) to define the configration of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''


    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #Read line from the files
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty space lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt is not found")
    
    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Ankit Sharma",
    author_email="ankit302290@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)