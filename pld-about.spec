Summary:	PLD-About
Summary(pl):	PLD-About
Name:		pld-about
Version:	0.1.4
Release:	3
License:	GPL
Group:		X11/Applications
Vendor:		Mariusz 'Ma-rYu-sH' Witkowski <maryush@pld.org.pl>
Source0:	PLD-About-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}-po.patch
URL:		http://www.pld.org.pl/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel < 2.0
BuildRequires:	gtk+-devel < 2.0
Requires:	XFree86-fonts-75dpi-ISO8859-2
Requires:	fonts-Type1-ulT1mo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Little program similar to gnome-about. It displays a list of the PLD
developers and other people that support distribution development.
This package contains GNOME version.

%description -l pl
Ma³y programik podobny do gnome-about, zawieraj±cy listê developerów i
osób wspó³pracuj±cych przy tworzeniu dystrybucji PLD. Wersja GNOME.

%prep
%setup -q -n PLD-About-%{version}
%patch0 -p1

%build
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__gettextize}
%{__automake}
%configure
mv po/pl/pld-about.po po/pl.po
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir},%{_datadir}/pld-about}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install lista.dat $RPM_BUILD_ROOT%{_datadir}/pld-about
install pld-about.desktop $RPM_BUILD_ROOT%{_applnkdir}
install pld-about.png $RPM_BUILD_ROOT%{_pixmapsdir}
install src/pld_logo2.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/pld-about
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/pld-about2.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pld-about
%{_applnkdir}/*.desktop
%{_pixmapsdir}/*
