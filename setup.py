from setuptools import find_packages, setup


def get_requirements()->list[str]:
    requirements_list = list[str] =[]
    return requirements_list

setup(
name='sensor',
version='0.0.2',
author='jeevan',
author_email='jeevanarande@gmail.com',
packages=find_packages(),
install_requires = get_requirements(),
)
