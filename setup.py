# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

import testprogram

setup(
        name="program",
        version=testprogram.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['tscript76 = testprogram.tscript76:main']
        }

)
