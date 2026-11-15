%define major 0
%define api 1.0

%define libname %mklibname tatsu %{api}
%define devname %mklibname -d tatsu


Summary:	Library for manipulating Apple Binary and XML Property Lists
Name:		libtatsu
Version:	1.1.0
Release:	%{?git:0.%{git}.}2
Group:		System/Libraries
License:	LGPLv2.1
Url:		https://www.libimobiledevice.org/
Source0:	https://github.com/libimobiledevice/libtatsu/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(libplist-2.0)

%description
Library handling the communication with Apple's Tatsu Signing Server (TSS).


%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for manipulating Apple Binary and XML Property Lists
Suggests:	%{name} >= %{version}-%{release}
Obsoletes:	%{name} < %{EVRD}

%description	-n %{libname}
Library handling the communication with Apple's Tatsu Signing Server (TSS).

%package  -n 	%{devname}
Summary:	Development package for libtatsu
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	 %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
echo %{version} > .tarball-version
./autogen.sh --prefix=/usr --libdir=/usr/lib64 --disable-static

%build
%make_build

%install
%make_install

#%files
#%%doc AUTHORS COPYING.LESSER
#%%{_mandir}/man1/plistutil.1*

%files -n  %{libname}
%{_libdir}/%{name}.so.%{major}{,.*}
 

%files -n  %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/%{name}.so


