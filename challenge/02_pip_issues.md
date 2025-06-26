# Challenge 02: Pip Installation Issues

## Background

We maintain a Python package called "chalkpy" that depends on psycopg2.

## Customer Issue

A customer writes:

> I am trying to install chalkpy, but I get an error about psycopg2. How do I fix this?
>
> I got this output:

```
× Failed to build `psycopg2==2.9.10`
├─▶ The build backend returned an error
╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit
status: 1)

[stdout]
running bdist_wheel
running build
running build_py
creating build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/__init__.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/_ipaddress.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/_json.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/_range.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/errorcodes.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/errors.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/extensions.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/extras.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/pool.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/sql.py -> build/lib.linux-x86_64-cpython-39/psycopg2
copying lib/tz.py -> build/lib.linux-x86_64-cpython-39/psycopg2
running build_ext
building 'psycopg2._psycopg' extension
creating build/temp.linux-x86_64-cpython-39/psycopg
clang -pthread -Wno-unused-result -Wsign-compare
-Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -fPIC
"-DPSYCOPG_VERSION=2.9.10 (dt dec pq3 ext lo64)" -DPSYCOPG_DEBUG=1
-DPG_VERSION_NUM=140017 -DHAVE_LO64=1 -DPSYCOPG_DEBUG=1
-I/home/runner/_work/_temp/setup-uv-cache/builds-v0/.tmpImQZEZ/include
-I/home/runner/.local/share/uv/python/cpython-3.9.22-linux-x86_64-gnu/include/python3.9
-I. -I/usr/include/postgresql -I/usr/include/postgresql/14/server
-I/usr/include/libxml2 -c psycopg/adapter_asis.c -o
build/temp.linux-x86_64-cpython-39/psycopg/adapter_asis.o
-Wdeclaration-after-statement

[stderr]
/home/runner/_work/_temp/setup-uv-cache/builds-v0/.tmpImQZEZ/lib/python3.9/site-packages/setuptools/dist.py:761:
SetuptoolsDeprecationWarning: License classifiers are deprecated.
!!


********************************************************************************
Please consider removing the following classifiers in favor of a
SPDX license expression:

License :: OSI Approved :: GNU Library or Lesser General Public
License (LGPL)

See
https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license
for details.

********************************************************************************

!!
self._finalize_license_expression()

It appears you are missing some prerequisite to build the package from
source.

You may install a binary package by installing 'psycopg2-binary' from
PyPI.
If you want to install psycopg2 from source, please install the packages
required for the build and try again.

For further information please check the 'doc/src/install.rst' file
(also at
<https://www.psycopg.org/docs/install.html>).

error: command 'clang' failed: No such file or directory

hint: This usually indicates a problem with the package or the build
environment.
help: `psycopg2` (v2.9.10) was included because `chalkpy[postgresql]`
(v2.74.3) depends on `psycopg2`
```

## Questions

1. Please research this problem and write an answer that might help the customer resolve the installation issue.

2. How should we deflect this question in the future to reduce support burden?