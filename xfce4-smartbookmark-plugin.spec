Summary:	Xfce panel smartbookmark plugin
Summary(pl):	Sprytne zak³adki dla Xfce panel
Name:		xfce4-smartbookmark-plugin
Version:	0.4.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	284e26595637dd2e900b75534372496b
URL:		http://goodies.xfce.org/
BuildRequires:	pkgconfig
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple plugin that lets the user send requests directly
to your browser and perform a custom search.

%description -l pl
Wtyczka ta pozwala na wysy³anie zapytañ bezpo¶rednio do zdefiniowanych
stron WWW.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/libsmartbookmark.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/xfce4/panel-plugins/libsmartbookmark.so
%{_datadir}/xfce4/panel-plugins/smartbookmark.desktop
