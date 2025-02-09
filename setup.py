from setuptools import setup

setup(name='pyyaml_demo',
      version='0.1',
      description='Contextual analysis example using PyYAML',
      author='JFrog',
      license='MIT',
      packages=['pyyaml_demo'],
      install_requires=[
          'PyYAML==6.0.1',
          'django-anymail==1.2.1',
      ])
