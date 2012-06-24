#
# TODO:
# - investigate the error while loading this module
#
%define		_module_name	tclock
%define		_snap	20060420
Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl):	Modu� Enlightenmenta DR17: %{_module_name}
Name:		enlightenment-module-%{_module_name}
Version:	0.2.1
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e_modules/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	4a473333232366812fb96bdfafc525fe
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenmentDR17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple text clock module for E17.

%description -l pl
Prosty modu� zegara tekstowego dla E17.

%prep
%setup -q -n %{_module_name}
sed -e 's|datadir=.*|datadir="`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_DATA_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`/${PACKAGE}"|' \
    -e '/PACKAGE_LIB_DIR/s|"[^"]*"|"`enlightenment-config --module-dir`"|' \
    -i configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_module_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_module_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules_extra/%{_module_name}/*.png
%{_libdir}/enlightenment/modules_extra/%{_module_name}/%{_module_name}.edj
