Summary:	PLD-About
Summary(pl):	PLD-About
Name:		pld-about
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Mariusz 'Ma-rYu-sH' Witkowski <maryush@pld.org.pl>
Source0:	PLD-About-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		%{name}.patch
URL:		http://www.pld.org.pl/
BuildRequires:	gnome-libs-devel < 2.0
BuildRequires:	gtk+-devel < 2.0
Requires:	XFree86-fonts-75dpi-ISO8859-2
Requires:	fonts-Type1-ulT1mo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Little program similar to gnome-about. It displays a list of the PLD
developers and other people that support distribution development.
This package contains GNOME version.

%description -l pl
Ma³y programik podobny do gnome-about, zawieraj±cy listê developerów i
osób wspó³pracuj±cych przy tworzeniu dystrybucji PLD. Wersja GNOME.

%prep
%setup -q -n PLD-About-%{version}
%patch -p1

%build
./autogen.sh
%configure

%{__make}
rm -f po/pl/*.mo
msgfmt -o po/%{name}.mo po/%{name}.po

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}
install pld-about.desktop $RPM_BUILD_ROOT%{_applnkdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES
install po/%{name}.mo $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/pld-about/pld_logo.xpm
%{_applnkdir}/*.desktop
%{_pixmapsdir}/*.png
