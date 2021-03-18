from setuptools import setup

setup(
    name='rdfdocgen',
    version='1.0.0',
    packages=['rdfdocgen'],
    url='https://github.com/kptyson/rdfdocgen',
    license='MIT License',
    author='Kevin Tyson',
    author_email='kevin.tyson@industrialsemantics.com',
    description='Create MS Word documentation from RDF files',
    install_requires=['click', 'rdflib', 'docx', 're', 'pandas', 'logging', 'os'],
    python_requires='>=3'
)
