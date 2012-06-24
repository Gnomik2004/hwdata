# TODO: use system {usb,pci}.ids (or symlink them)?
Summary:	Hardware identification and configuration data
Summary(pl):	Dane do identyfikacji i konfiguracji sprz�tu
Name:		hwdata
Version:	0.169
Release:	1
License:	GPL/XFree86
Group:		Applications/System
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	98838e0f541b362cb3bd129984ba0c2a
Requires:	pciutils
Conflicts:	Xconfigurator < 4.9.42-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hwdata contains various hardware identification and configuration
data, such as the pci.ids database, the XFree86 Cards and MonitorsDB
databases.

%description -l pl
Pakiet hwdata zawiera r�ne dane do identyfikacji i konfiguracji
sprz�tu, takie jak baza danych pci.ids oraz bazy Cards i MonitorsDB
dla XFree86.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

rm -f pci.ids

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -s /etc/pci.ids $RPM_BUILD_ROOT%{_datadir}/hwdata/pci.ids

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{_datadir}/hwdata
