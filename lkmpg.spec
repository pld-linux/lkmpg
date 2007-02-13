Summary:	LDP Linux Kernel Module Programming Guide
Summary(pl.UTF-8):	Podręcznik pisania modułów do jądra Linuksa
Name:		lkmpg
Version:	2.6.3
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/lkmpg/2.6/%{name}.html.tar.gz
# Source0-md5:	a062c70959bea6adc785fd57bcaadb89
URL:		http://www.tldp.org/LDP/lkmpg/2.6/html/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is for people who want to write Linux kernel modules.

%description -l pl.UTF-8
Dokument dla ludzi chcących pisać moduły do jądra Linuksa.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
