Summary:	Toolbar for Google search engine
Summary(pl.UTF-8):   Pasek narzędziowy dla wyszukiwarki Google
Name:		mozilla-addon-googlebar
%define		_realname	googlebar
Version:	0.8
%define	fver	0_8
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east3.mozdev.org/%{_realname}/%{fver}.xpi
# Source0-md5:	c321bb115f0fe503f27fefe01de36eb8
Source1:	%{_realname}-installed-chrome.txt
URL:		http://googlebar.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Extended toolbar for Google search engine. It supports all features
of Google, Google Groups etc.

%description -l pl.UTF-8
Rozbudowany pasek narzędziowy z dla wyszukiwarki Google. Można
korzystać z wszystkich możliwości Google, Google Groups itd...

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
zip -r -9 -m ../%{_realname}.jar ./
cd -
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
