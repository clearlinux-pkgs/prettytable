#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : prettytable
Version  : 0.7.2
Release  : 58
URL      : http://pypi.debian.net/prettytable/prettytable-0.7.2.tar.gz
Source0  : http://pypi.debian.net/prettytable/prettytable-0.7.2.tar.gz
Summary  : A simple Python library for easily displaying tabular data in a visually appealing ASCII table format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: prettytable-license = %{version}-%{release}
Requires: prettytable-python = %{version}-%{release}
Requires: prettytable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
TUTORIAL ON HOW TO USE THE PRETTYTABLE 0.6+ API
*** This tutorial is distributed with PrettyTable and is meant to serve
as a "quick start" guide for the lazy or impatient.  It is not an
exhaustive description of the whole API, and it is not guaranteed to be
100% up to date.  For more complete and update documentation, check the
PrettyTable wiki at http://code.google.com/p/prettytable/w/list ***

%package license
Summary: license components for the prettytable package.
Group: Default

%description license
license components for the prettytable package.


%package python
Summary: python components for the prettytable package.
Group: Default
Requires: prettytable-python3 = %{version}-%{release}

%description python
python components for the prettytable package.


%package python3
Summary: python3 components for the prettytable package.
Group: Default
Requires: python3-core
Provides: pypi(prettytable)
Requires: pypi(setuptools)
Requires: pypi(wcwidth)

%description python3
python3 components for the prettytable package.


%prep
%setup -q -n prettytable-0.7.2
cd %{_builddir}/prettytable-0.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603399294
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/prettytable
cp %{_builddir}/prettytable-0.7.2/COPYING %{buildroot}/usr/share/package-licenses/prettytable/13c8cd668dfb0aa6e5485b8b46dd0b29abbb497e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/prettytable/13c8cd668dfb0aa6e5485b8b46dd0b29abbb497e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
