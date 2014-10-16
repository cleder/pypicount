from setuptools import setup, find_packages
import sys, os
from setuptools.command.test import test as TestCommand

version = '0.0'

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name='pypicount',
      version=version,
      description="Count download pypi packages",
      long_description=open('README.rst').read(),
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
      ],
      keywords='pypi cheeseshop',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='http://github.com/cleder/pypicount',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      tests_require=['pytest'],
      cmdclass = {'test': PyTest},
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
