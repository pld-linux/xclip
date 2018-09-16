Summary:	An interface to X selections ("the clipboard")
Summary(pl.UTF-8):	Interfejs do schowka X Window System
Name:		xclip
Version:	0.13
Release:	1
Epoch:		0
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/astrand/%{name}/archive/%{version}.tar.gz
# Source0-md5:	81e49f56288f299e3389a019f2550ad2
URL:		https://github.com/astrand/xclip
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXmu-devel
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
%{__autoconf}
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
%attr(755,root,root) %{_bindir}/xclip
%attr(755,root,root) %{_bindir}/xclip-copyfile
%attr(755,root,root) %{_bindir}/xclip-cutfile
%attr(755,root,root) %{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip.1*
%{_mandir}/man1/xclip-copyfile.1*
