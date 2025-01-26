from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            # requirements.append('pip install -U -r requirements.txt')
    return requirements

setup(
    name="ML project",
    version="0.0.1",
    author="Yubaraj",
    author_email="yubarajsingha2808@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
