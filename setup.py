# -*- coding: utf-8 -*-

import codecs
from setuptools import setup

with codecs.open('README', encoding='utf-8') as f:
    readme_text = f.read()


setup(
    name='mgrspy',
    version='0.3.1',
    install_requires=['pyproj>=1.9.5', 'future'],
    author='Planet Federal',
    author_email='info@federal.planet.com',
    description='Convert WGS84 coordinates to MGRS and back',
    long_description=readme_text,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: '
        'GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    license="GPLv2+",
    keywords='mgrs wgs gis coordinate conversion',
    url='https://github.com/planetfederal/mgrspy',
    package_dir={'': '.'},
    test_suite='tests.suite',
    packages=['mgrspy'],
    python_requires='>=2.7, >=3.4, <4',
)
