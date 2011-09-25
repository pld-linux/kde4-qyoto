%define         _state          stable
%define         orgname         qyoto
%define         qtver           4.7.4

Summary:	C# Mono Qt4 bindings
Summary(pl.UTF-8):	Dowiązania C# Mono dla Qt4
Name:		qyoto
Version:	4.7.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	7c81786e0f80353d8fd7e11ce4471272
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	mono-csharp
BuildRequires:	phonon-devel
BuildRequires:	qimageblitz-devel
BuildRequires:	qscintilla2-devel
BuildRequires:	smokeqt-devel
Obsoletes:	kde4-kdebindings-qyoto < 4.6.100
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C# Mono Qt4 bindings.

%description -l pl.UTF-8
Dowiązania C# Mono dla Qt4.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kde4-kdebindings-qyoto-devel < 4.7.0

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqyoto.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqyoto.so.?
%attr(755,root,root) %{_libdir}/libphonon-sharp.so
%attr(755,root,root) %{_libdir}/libqtscript-sharp.so
%attr(755,root,root) %{_libdir}/libqttest-sharp.so
%attr(755,root,root) %{_libdir}/libqtuitools-sharp.so
%attr(755,root,root) %{_libdir}/libqtwebkit-sharp.so
%attr(755,root,root) %{_libdir}/libqscintilla-sharp.so
%dir %{_prefix}/lib/mono/qyoto
%{_prefix}/lib/mono/qyoto/phonon.dll
%{_prefix}/lib/mono/qyoto/qscintilla.dll
%{_prefix}/lib/mono/qyoto/qt-dotnet.dll
%{_prefix}/lib/mono/qyoto/qtscript.dll
%{_prefix}/lib/mono/qyoto/qttest.dll
%{_prefix}/lib/mono/qyoto/qtuitools.dll
%{_prefix}/lib/mono/qyoto/qtwebkit.dll
%{_prefix}/lib/mono/gac/phonon
%{_prefix}/lib/mono/gac/qscintilla
%{_prefix}/lib/mono/gac/qt-dotnet
%{_prefix}/lib/mono/gac/qtscript
%{_prefix}/lib/mono/gac/qttest
%{_prefix}/lib/mono/gac/qtuitools
%{_prefix}/lib/mono/gac/qtwebkit

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/csrcc
%attr(755,root,root) %{_bindir}/uics
%attr(755,root,root) %{_libdir}/libqyoto.so
%{_includedir}/qyoto
%{_pkgconfigdir}/qyoto.pc
%{_pkgconfigdir}/qtscript-sharp.pc
%{_pkgconfigdir}/qttest-sharp.pc
%{_pkgconfigdir}/qtuitools-sharp.pc
%{_pkgconfigdir}/qtwebkit-sharp.pc
%{_datadir}/qyoto