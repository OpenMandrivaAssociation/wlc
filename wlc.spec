%define major	0
%define libname	%mklibname wlc %{major}

%define devname	%mklibname -d wlc
%define snapshot	20170213

Summary:        Wayland compositor library
Name:           wlc
Version:        0.0.7
%if "%{snapshot}" != ""
%define tarname	%{name}-%{version}-%{snapshot}
Release:        0.%{snapshot}.1
Source0:	%{name}-%{version}-%{snapshot}.tar.xz
%else
Release:	1
Source0:	https://github.com/Cloudef/wlc/releases/download/v%{version}/%{name}-%{version}.tar.bz2
%define	tarname	%{name}-%{version}
%endif

License:        GPLv2+
Url:            https://github.com/Cloudef

BuildRequires:	cmake
BuildRequires:	pixman-devel
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(wayland-egl)
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(chck)

%description
Wayland compositor library

%package -n	%{libname}
Summary:	Library for accessing Wayland
Group:		System/Libraries

%description -n	%{libname}
Wayland compositor library

#################################

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -qn %{tarname}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWLC_BUILD_TESTS=OFF
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libwlc.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libwlc.so
%{_libdir}/pkgconfig/wlc.pc
