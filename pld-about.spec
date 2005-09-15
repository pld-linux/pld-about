%include	/usr/lib/rpm/macros.mono
Summary:	PLD About
Summary(pl):	O PLD
Name:		pld-about
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://team.pld-linux.org/~wolf/%{name}-%{version}.tar.bz2
# Source0-md5:	d9d5cd6dcbe42def0e5b80f9f34e6454
URL:		http://www.pld-linux.org/
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.5.91-2
BuildRequires:	gettext-devel
BuildRequires:	mono-csharp >= 1.1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Little program showing information about PLD developers.

%description -l pl
Ma³y program wy¶wietlaj±cy informacje o twórcach PLD.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_libdir}/pld-about/backgrounds}

install gdk-cairo.dll pld-about.exe front.png bociek.png \
		$RPM_BUILD_ROOT%{_libdir}/pld-about
install backgrounds/* $RPM_BUILD_ROOT%{_libdir}/pld-about/backgrounds

install pld-about.desktop	$RPM_BUILD_ROOT%{_desktopdir}
install resources/icon64.png	$RPM_BUILD_ROOT%{_pixmapsdir}/pld-about.png

for i in locale/*.mo
do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/`basename $i .mo`/LC_MESSAGES
	install $i $RPM_BUILD_ROOT%{_datadir}/locale/`basename $i .mo`/LC_MESSAGES/pld-about.mo
done

cat > $RPM_BUILD_ROOT%{_bindir}/pld-about << EOF
#!/bin/sh
cd %{_libdir}/pld-about
exec /usr/bin/mono %{_libdir}/pld-about/pld-about.exe "\$@"
EOF

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/{ChangeLog,copyrights,kryteria,skrypty}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/pld-about
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
