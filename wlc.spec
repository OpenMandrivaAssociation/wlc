%define major	0
%define libname	%mklibname wlc %{major}
%define libchck_atlas	%mklibname chck-atlas %{major}
%define libchck_buffer	%mklibname chck-buffer %{major}
%define libchck_dl	%mklibname chck-dl %{major}
%define libchck_fs	%mklibname chck-fs %{major}
%define libchck_lut	%mklibname chck-lut %{major}
%define libchck_pool	%mklibname chck-pool %{major}
%define libchck_sjis	%mklibname chck-sjis %{major}
%define libchck_string	%mklibname chck-string %{major}
%define libchck_tqueue	%mklibname chck-tqueue %{major}
%define libchck_unicode	%mklibname chck-unicode %{major}
%define libchck_xdg	%mklibname chck-xdg %{major}

%define devname	%mklibname -d wlc
%define devchck	%mklibname -d chck

%define date	20160427

Summary:        Wayland compositor library
Name:           wlc
Version:        0.0.5
Release:        1
License:        GPLv2+
Url:            https://github.com/Cloudef/wlc/
Source0:	https://github.com/Cloudef/wlc/releases/download/v0.0.5/%{name}-%{version}.tar.bz2
Source1:	chck-%{date}.tar.xz
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

%description
Wayland compositor library

%package -n	%{libname}
Summary:	Library for accessing Wayland
Group:		System/Libraries

%description -n	%{libname}
Wayland compositor library

#################################
%package -n	%{libchck_atlas}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_atlas}
Support libs for %{name}
#################################

%package -n	%{libchck_buffer}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_buffer}
Support libs for %{name}

#################################

%package -n	%{libchck_dl}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_dl}
Support libs for %{name}

#################################

%package -n	%{libchck_fs}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_fs}
Support libs for %{name}

#################################

%package -n	%{libchck_lut}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_lut}
Support libs for %{name}

#################################
%package -n	%{libchck_pool}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_pool}
Support libs for %{name}

#################################
%package -n	%{libchck_sjis}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_sjis}
Support libs for %{name}

#################################
%package -n	%{libchck_string}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_string}
Support libs for %{name}

#################################
%package -n	%{libchck_tqueue}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_tqueue}
Support libs for %{name}

#################################
%package -n	%{libchck_unicode}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_unicode}
Support libs for %{name}

#################################

%package -n	%{libchck_xdg}
Summary:	Library for chck
Group:		System/Libraries

%description -n	%{libchck_xdg}
Support libs for %{name}

#################################

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%package -n	%{devchck}
Summary:	Development files for chck and %{name}
Group:		Development/C++
Requires:	%{libchck_atlas} = %{EVRD}
Requires:	%{libchck_buffer} = %{EVRD}
Requires:	%{libchck_dl} = %{EVRD}
Requires:	%{libchck_fs} = %{EVRD}
Requires:	%{libchck_lut} = %{EVRD}
Requires:	%{libchck_pool} = %{EVRD}
Requires:	%{libchck_sjis} = %{EVRD}
Requires:	%{libchck_string} = %{EVRD}
Requires:	%{libchck_tqueue} = %{EVRD}
Requires:	%{libchck_unicode} = %{EVRD}
Requires:	%{libchck_xdg} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -q -a 1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWLC_BUILD_TESTS=OFF -DSOURCE_WLPROTO=ON
%make
cd ../
pushd chck-%{date}
%cmake
%make


%install
%makeinstall_std -C build
%makeinstall_std -C chck-%{date}/build

%files -n %{libname}
%{_libdir}/libwlc.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libwlc.so
%{_libdir}/pkgconfig/wlc.pc

%files -n %{devchck}
%{_includedir}/chck
%{_libdir}/libchck-*.so
%{_libdir}/pkgconfig/chck.pc

%files -n %{libchck_atlas}
%{_libdir}/libchck-atlas.so.%{major}*

%files -n %{libchck_buffer}
%{_libdir}/libchck-buffer.so.%{major}*

%files -n %{libchck_dl}
%{_libdir}/libchck-dl.so.%{major}*

%files -n %{libchck_fs}
%{_libdir}/libchck-fs.so.%{major}*

%files -n %{libchck_lut}
%{_libdir}/libchck-lut.so.%{major}*

%files -n %{libchck_pool}
%{_libdir}/libchck-pool.so.%{major}*

%files -n %{libchck_sjis}
%{_libdir}/libchck-sjis.so.%{major}*

%files -n %{libchck_string}
%{_libdir}/libchck-string.so.%{major}*

%files -n %{libchck_tqueue}
%{_libdir}/libchck-tqueue.so.%{major}*

%files -n %{libchck_unicode}
%{_libdir}/libchck-unicode.so.%{major}*

%files -n %{libchck_xdg}
%{_libdir}/libchck-xdg.so.%{major}*
