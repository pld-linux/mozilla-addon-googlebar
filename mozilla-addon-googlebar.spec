Summary:        Toolbar for google search engine
Summary(pl):    PAsek narzêdziowy dla wyszukiwarki google
Name:           mozilla-addon-googlebar
Version:        0.4.5RC
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://googlebar.mozdev.org/googlebar_045RC.xpi
Source1:        googlebar-installed-chrome.txt
URL:            http://googlebar.mozdev.org/
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	googlebar

%description
%description -l pl
Rozbudowany pasek narzêdziowy z dla wyszukiwarki google. Mo¿na korzystaæ z
wszystkich mo¿liwo¶ci Google, Google Groups itd...

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "googlebar" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
