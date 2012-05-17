Summary:	Xfce panel smartbookmark plugin
Summary(pl.UTF-8):	Sprytne zakładki dla Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.4.4
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-smartbookmark-plugin/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	273e38306a82f14e1b8c2c5db912f6c3
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-smartbookmark-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple plugin that lets the user send requests directly to
your browser and perform a custom search.

%description -l pl.UTF-8
Wtyczka ta pozwala na wysyłanie zapytań bezpośrednio do zdefiniowanych
stron WWW.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/libsmartbookmark.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/libsmartbookmark.so
%{_datadir}/xfce4/panel-plugins/smartbookmark.desktop
