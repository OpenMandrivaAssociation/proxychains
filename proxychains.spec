%define name proxychains
%define version 3.1
%define release %mkrel 5
%define major 3
%define libname %mklibname %name %major
%define develname %mklibname %name -d 

Name: 		%{name} 
Version: 	%{version}
Release: 	%{release}
Summary: 	This program forces any tcp connection to follow through proxy
License: 	GPL
Group: 		Networking/Other 
URL:		http://proxychains.sourceforge.net
Source:  	http://prdownloads.sourceforge.net/proxychains/%{name}-%{version}.tar.gz
Patch0:		proxychains-3.1-ld_preload.patch
BuildRoot:  %{_tmppath}/%{name}-%{version}


%package -n %libname
Summary:    This program forces any tcp connection to follow through proxy
Group:      System/Libraries
Obsoletes:	%{_lib}proxychains1 < 3.1-5

%package -n %develname
Summary:    This program forces any tcp connection to follow through proxy
Group:      Development/Other
Requires:	%{libname} = %{version}-%{release}

%description
This program forces any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / permeo / eborder driver ( intercepts TCP calls )
It is FREE.
This version (1.8.x)  supports SOCKS4, SOCKS5 and HTTP CONNECT proxy servers.
Auth-types: socks - "user/pass" , http - "basic".

%description -n %libname
This program forces any tcp connection made by any given tcp client
to follow through proxy (or proxy chain). It is a kind of proxifier.
It acts like sockscap / permeo / eborder driver ( intercepts TCP calls )
It is FREE.
This version (1.8.x)  supports SOCKS4, SOCKS5 and HTTP CONNECT proxy servers.
Auth-types: socks - "user/pass" , http - "basic".

%description -n %develname
Devel package for proxychains.

%prep
%setup -q 
%patch0 -p1

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}  

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files 
%defattr(-,root,root)  
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
