Summary:	LDP Linux Kernel Module Programming Guide
Summary(pl):	Podrêcznik pisania modu³ów do kernela
Name:		lkmpg
Version:	1.1.0
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
URL:		http://www.tldp.org/LDP/lkmpg/mpg.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document is for people who want to write kernel modules.

%description -l pl
Dokument dla ludzi chc±cych pisaæ modu³y do kernela.

%prep
%setup -q -n %{name}-%{version}.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
