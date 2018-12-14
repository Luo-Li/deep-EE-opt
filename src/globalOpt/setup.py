#!/usr/bin/env python3

# Copyright (C) 2018 Bho Matthiesen
# 
# This program is used in the article:
# 
# Bho Matthiesen, Alessio Zappone, Eduard A. Jorswieck, and Merouane Debbah,
# "Deep Learning for Optimal Energy-Efficient Power Control in Wireless
# Interference Networks," submitted to IEEE Journal on Selected Areas in
# Communication.
# 
# License:
# This program is licensed under the GPLv2 license. If you in any way use this
# code for research that results in publications, please cite our original
# article listed above.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = [Extension(
            name='wseePy',
            sources = ['wseePy.pyx'],
            include_dirs = ['.','/opt/intel/compilers_and_libraries/linux/mkl/include','lambert_w/include'],
            library_dirs = ['./', '/opt/intel/compilers_and_libraries/linux/mkl/lib/intel64'],
            #runtime_library_dirs = ['./'],
            extra_objects = ['util.o'],
            libraries = ['mkl_rt','m',],
            language = "c++",
            extra_compile_args = ["-std=c++17", '-fpic', "-O3", '-march=haswell', '-mtune=haswell', '-DNDEBUG', '-m64', '-fopenmp'],
            extra_link_args = ["-std=c++17", '-Wl,--no-as-needed', '-fopenmp']),
        ]

setup(
    ext_modules = cythonize(exts)
)
