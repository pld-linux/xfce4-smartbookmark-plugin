Summary:	Xfce panel smartbookmark plugin
Summary(pl.UTF-8):	Sprytne zakładki dla Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.5.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-smartbookmark-plugin/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	8be187c4a4ef0ecc16f1e039b255a988
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-smartbookmark-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	exo
Requires:	xfce4-panel >= 4.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple plugin that lets the user send requests directly to
your browser and perform a custom search.

%description -l pl.UTF-8
Wtyczka ta pozwala na wysyłanie zapytań bezpośrednio do zdefiniowanych
stron WWW.

%prep
%setup -q

%{__sed} -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libsmartbookmark.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libsmartbookmark.so
%{_datadir}/xfce4/panel/plugins/smartbookmark.desktop
