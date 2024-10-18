# setup.py
from setuptools import setup, find_packages

setup(
    name="habibi",
    version="0.0.1-rc.0",
    packages=find_packages(),
    install_requires=[],
    author="Biplav",
    author_email="your-email@example.com",
    description="A sample Python project",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my_sample_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
