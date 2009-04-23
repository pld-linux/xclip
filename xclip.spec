Summary:	An interface to X selections ("the clipboard")
Summary(pl.UTF-8):	Interfejs do schowka X Window System
Name:		xclip
Version:	0.11
Release:	1
Epoch:		0
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xclip/%{name}-%{version}.tar.gz
# Source0-md5:	4caf3a2b03c36981f9af36a8e8582951
URL:		http://sourceforge.net/projects/xclip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xclip is a command line utility that provides an interface to X
selections ("the clipboard"). It can read data from standard in or a
file and place it in an X selection for pasting into other X
applications. xclip can also print an X selection to standard out,
which can then be redirected to a file or another program.

%description -l pl.UTF-8
xclip jest narzędziem linii poleceń dostarczającym interfejsu do
schowka X Window System. Może czytać dane ze standardowego wejścia lub
pliku i wstawiać je do schowka X w celu wklejenia do innych aplikacji.
Może również wypisać zawartość schowka na standardowe wyjście, które
następnie można przekierować do pliku lub innego programu.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_mandir}/man*/*
