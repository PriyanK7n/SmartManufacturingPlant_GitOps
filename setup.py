from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOps-Smart-Manufacturing-Project",
    
    version = "0.1",
    
    author = "Priyank",
    
    packages = find_packages(),
    
    install_requires = requirements
)