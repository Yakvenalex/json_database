from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='json-db-lite',
    version='0.1.0',
    description='A simple JSON file database manager',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Alexey Yakovenko',
    author_email='mr.mnogo@gmail.com',
    url='https://github.com/Yakvenalex/json_database',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
