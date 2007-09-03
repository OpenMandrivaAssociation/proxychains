%define name proxychains
%define version 1.8.2
%define release 2mdk
%define major 1
%define libname %mklibname %name %major

Name: 		%{name} 
Summary: 	This program forces any tcp connection to follow through proxy.
Version: 	%{version}
Release: 	%{release}
Source:  	%{name}-%{version}.tar.bz2	
Patch0:		proxychains_gccbuild.patch.bz2
Group: 		Networking/Other 
URL:		http://proxychains.sourceforge.net
BuildRoot:      %{_tmppath}/%{name}-buildroot  
Requires: libproxychains1 = 1.8.2-2mdk

License: 	GPL

%package -n %libname
Summary: This program forces any tcp connection to follow through proxy.
Group:  System/Libraries
Provides: libproxychains

%package -n %libname-devel
Summary: This program forces any tcp connection to follow through proxy.
Group: Development/Other
Provides: libproxychains-devel
Requires: libproxychains1 = 1.8.2-2mdk

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

%description -n %libname-devel
Devel package for proxychains.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%patch0 -p1

cat ./proxychains/Makefile.in | sed -e "s#\$(mkinstalldirs) /etc/#\$(mkinstalldirs) \$(sysconfdir)/#g" | sed -e "s#\$(INSTALL_DATA) \$(srcdir)/proxychains.conf /etc/proxychains.conf#\$(INSTALL_DATA) \$(srcdir)/proxychains.conf \$(sysconfdir)/proxychains.conf#g" > ./proxychains/Makefile.in.new
mv ./proxychains/Makefile.in.new ./proxychains/Makefile.in
%build
cat ./proxychains/main.c | sed -e "s#/usr/lib/libproxychains.so#/usr/lib/libproxychains.so.1#g" > ./proxychains/main.c.new
mv ./proxychains/main.c.new ./proxychains/main.c
%configure --prefix=%buildroot/usr --sysconfdir=%buildroot/etc

%make

%install
%makeinstall 
%clean
rm -rf $RPM_BUILD_ROOT  
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%files 
%defattr(-,root,root)  
%doc README AUTHORS COPYING ChangeLog
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*

%files -n %libname
%defattr(-,root,root,-)  
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root,-)  
%{_libdir}/*.la
%{_libdir}/*.so

