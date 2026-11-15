%define major 0
%define api 1.0

%define libname %mklibname tatsu 
%define devname %mklibname -d tatsu


Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libtatsu
Version:	1.1.0
Release:	%{?git:0.%{git}.}2
Group:		System/Libraries
License:	LGPLv2.1
Url:		https://www.libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libtatsu/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(libplist-2.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	slibtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildSystem:	autotools
BuildOption:	--disable-static

%description
Library handling the communication with Apple's Tatsu Signing Server (TSS).


%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Obsoletes:	%{name} < %{EVRD}

%description	-n %{libname}
Library handling the communication with Apple's Tatsu Signing Server (TSS).

%package  -n 	%{devname}
Summary:	Development package for libtatsu
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	 %{devname}
Development files (Headers etc.) for %{name}.

%prep -a
echo %{version} > .tarball-version
sed -i -e 's,libtool,slibtool,g' autogen.sh
NOCONFIGURE=1 ./autogen.sh

#%files
#%%doc AUTHORS COPYING.LESSER
#%%{_mandir}/man1/plistutil.1*

%files -n  %{libname}
%{_libdir}/%{name}.so.%{major}{,.*}


%files -n  %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}.so


