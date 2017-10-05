#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prettytable
Version  : 0.7.2
Release  : 28
URL      : http://pypi.debian.net/prettytable/prettytable-0.7.2.tar.gz
Source0  : http://pypi.debian.net/prettytable/prettytable-0.7.2.tar.gz
Summary  : A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prettytable-legacypython
Requires: prettytable-python3
Requires: prettytable-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
TUTORIAL ON HOW TO USE THE PRETTYTABLE 0.6+ API
*** This tutorial is distributed with PrettyTable and is meant to serve
as a "quick start" guide for the lazy or impatient.  It is not an
exhaustive description of the whole API, and it is not guaranteed to be
100% up to date.  For more complete and update documentation, check the
PrettyTable wiki at http://code.google.com/p/prettytable/w/list ***

%package legacypython
Summary: legacypython components for the prettytable package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the prettytable package.


%package python
Summary: python components for the prettytable package.
Group: Default
Requires: prettytable-legacypython
Requires: prettytable-python3

%description python
python components for the prettytable package.


%package python3
Summary: python3 components for the prettytable package.
Group: Default
Requires: python3-core

%description python3
python3 components for the prettytable package.


%prep
%setup -q -n prettytable-0.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507164395
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507164395
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
