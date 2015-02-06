%define major 3
%define libname %mklibname %name %major
%define develname %mklibname %name -d 

Name:		proxychains
Version:	3.1
Release:	8
Summary:	This program forces any tcp connection to follow through proxy
License:	GPL
Group:		Networking/Other 
URL:		http://proxychains.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/proxychains/%{name}-%{version}.tar.gz
Patch0:		proxychains-3.1-ld_preload.patch
Patch1:		glibc215.patch
Requires:	%{libname} = %{EVRD}

%package -n %{libname}
Summary:	This program forces any tcp connection to follow through proxy
Group:		System/Libraries
Obsoletes:	%{_lib}proxychains1 < 3.1-5

%package -n %{develname}
Summary:	This program forces any tcp connection to follow through proxy
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description
This program forces any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / permeo / eborder driver ( intercepts TCP calls )
It is FREE.
This version (1.8.x)  supports SOCKS4, SOCKS5 and HTTP CONNECT proxy servers.
Auth-types: socks - "user/pass" , http - "basic".

%description -n %{libname}
This program forces any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / permeo / eborder driver ( intercepts TCP calls )
It is FREE.
This version (1.8.x)  supports SOCKS4, SOCKS5 and HTTP CONNECT proxy servers.
Auth-types: socks - "user/pass" , http - "basic".

%description -n %{develname}
Devel package for proxychains.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
%configure2_5x

%make

%install
%makeinstall_std

%files 
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so

