#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prettytable
Version  : 0.7.2
Release  : 13
URL      : https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.gz
Source0  : https://pypi.python.org/packages/source/P/PrettyTable/prettytable-0.7.2.tar.gz
Summary  : A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prettytable-python
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

%package python
Summary: python components for the prettytable package.
Group: Default

%description python
python components for the prettytable package.


%prep
%setup -q -n prettytable-0.7.2

%build
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
%{__python} setup.py test
%install
rm -rf %{buildroot}
python3 setup.py install --root=%{buildroot}
python3 setup.py clean
python setup.py build
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
