%define major	0
%define libname	%mklibname wlc %{major}
%define devname	%mklibname -d wlc

Summary:        Wayland compositor library
Name:           wlc
Version:        0.0.2
Release:        1
License:        GPLv2+
Url:            https://github.com/Cloudef/wlc/
Source0:	https://github.com/Cloudef/wlc/releases/download/v0.0.2/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(libsystemd-login)
BuildRequires:	pkgconfig(zlib)

%description
Wayland compositor library

%package -n	%{libname}
Summary:	Library for accessing Wayland
Group:		System/Libraries

%description -n	%{libname}
Wayland compositor library

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%check
%make test

%files -n %{libname}
%{_libdir}/libwlc.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libwlc.so
%{_libdir}/pkgconfig/wlc.pc
