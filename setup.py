from setuptools import find_packages, setup
from typing import List 

hypen_e_dot='-e .'

def get_req(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

    return requirements


setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A short description of the project.',
    author='DT',
    license='',
    install_requires=get_req('requirements.txt')
)
