Summary:	Toolbar for Google search engine
Summary(pl):	Pasek narzêdziowy dla wyszukiwarki Google
Name:		mozilla-addon-googlebar
%define		_realname	googlebar
Version:	0.4.5RC
%define	fver	%(echo %{version} | tr -d .)
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://googlebar.mozdev.org/%{_realname}_%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://googlebar.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Extended toolbar for Google search engine. It supports all features
of Google, Google Groups etc.

%description -l pl
Rozbudowany pasek narzêdziowy z dla wyszukiwarki Google. Mo¿na
korzystaæ z wszystkich mo¿liwo¶ci Google, Google Groups itd...

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
