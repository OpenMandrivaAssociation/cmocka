%define major 0
%define libname %mklibname cmocka %{major}
%define devname %mklibname cmocka -d
%define _disable_lto 1

Summary:	C Unit Testing Framework
Name:		cmocka
Version:	1.1.7
Release:	1
License:	BSD-like
Group:		System/Libraries
Url:		https://cmocka.org/
Source0:	https://cmocka.org/files/%(echo %{version} |cut -d. -f1-2)/cmocka-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja

%description
cmocka is a unit testing framework for C with support for mock objects.
It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

%package -n	%{libname}
Summary:	A library of functions for running cmocka unit tests
Group:		System/Libraries

%description -n	%{libname}
cmocka is a unit testing framework for C with support for mock objects.
It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

%package -n	%{devname}
Summary:	Development tools for the cmocka unit test framework
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
cmocka is a unit testing framework for C with support for mock objects.
It only requires the standard C library, works on a range of computing
platforms (including embedded) and with different compilers.

%prep
%setup -q
%autopatch -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libcmocka.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/cmocka
