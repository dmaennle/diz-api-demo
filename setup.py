from setuptools import setup, find_packages

setup(
    name='diz',
    version='0.1',
    packages=find_packages(),
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/yourusername/diz',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)