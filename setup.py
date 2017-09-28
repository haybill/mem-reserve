#!/usr/bin/python3

from distutils.core import setup

setup(name='mem-reserve',
      version='1.0',
      description='Compute memory reservation parameters',
      author='Keith Packard',
      author_email='keithp@keithp.com',
      url='https://github.com/FabricAttachedMemory/mem-reserve',
      scripts=['mem-reserve'],
      data_files=[('share/man/man1', ['mem-reserve.1'])]
     )
