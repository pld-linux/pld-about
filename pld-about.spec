Summary:	PLD-About
Summary(pl):	PLD-About
Name:		pld-about
Version:	0.1.3
Release:	1
License:	GNU GPL
Group:		X11/Applications
Vendor:		Mariusz 'Ma-rYu-sH' Witkowski <maryush@pld.org.pl>
Source0:	PLD-About-%{version}.tar.gz
URL:		www.pld.org.pl
BuildRequires:	gtk+-devel < 2.0
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel < 2.0
Requires:	XFree86-fonts-75dpi-ISO8859-2
Requires:	fonts-Type1-ulT1mo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description -l pl
Ma�y programik podobny do gnome-about, zawieraj�cy list� developer�w i
os�b wsp�pracuj�cych przy tworzeniu dystrybucji PLD. Wersja GTK+.

%prep
%setup -q -n PLD-About-%{version}

%build
./autogen.sh
%configure \
    --prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}
install pld-about.desktop $RPM_BUILD_ROOT%{_applnkdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/pld-about/pld_logo.xpm
%{_applnkdir}/*.desktop
