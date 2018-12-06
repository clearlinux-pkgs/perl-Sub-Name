#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Name
Version  : 0.21
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Sub-Name-0.21.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Sub-Name-0.21.tar.gz
Summary  : '(Re)name a sub'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Name-lib = %{version}-%{release}
Requires: perl-Sub-Name-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Sub-Name,
version 0.21:
(Re)name a sub
This software is copyright (c) 2004 by Matthijs van Duin and cPanel Inc.

%package dev
Summary: dev components for the perl-Sub-Name package.
Group: Development
Requires: perl-Sub-Name-lib = %{version}-%{release}
Provides: perl-Sub-Name-devel = %{version}-%{release}

%description dev
dev components for the perl-Sub-Name package.


%package lib
Summary: lib components for the perl-Sub-Name package.
Group: Libraries
Requires: perl-Sub-Name-license = %{version}-%{release}

%description lib
lib components for the perl-Sub-Name package.


%package license
Summary: license components for the perl-Sub-Name package.
Group: Default

%description license
license components for the perl-Sub-Name package.


%prep
%setup -q -n Sub-Name-0.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Name
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-Sub-Name/LICENCE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Sub/Name.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Name.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Sub/Name/Name.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Name/LICENCE
