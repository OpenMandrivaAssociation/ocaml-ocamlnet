%define up_name ocamlnet
%define name    ocaml-%{up_name}

Name:           %{name}
Version:        3.6.3
Release:        1
Summary:        OCaml internet protocols and conventions
License:        BSD
Group:          Development/Other
URL:            http://projects.camlcity.org/projects/ocamlnet.html
Source:         http://download.camlcity.org/download/ocamlnet-%{version}.tar.gz
Patch0:         %{name}-3.6.1-destdir.patch
Patch1:         %{name}-3.6.1-fix-shm-test.patch
Patch2:         %{name}-2.2.9-fix-build.patch
BuildRequires:  ocaml >= 3.10.2
BuildRequires:  camlp4
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ncurses-devel

BuildRequires:  ocaml-ssl-devel
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  pcre-devel
BuildRequires:  openssl-devel
BuildRequires:  tcl-devel
BuildRequires:  ocaml-cryptgps-devel

Requires:       ocaml-pcre

%description
Ocamlnet is an ongoing effort to collect modules, classes and
functions that are useful to implement network protocols. Since
version 2.2, Ocamlnet incorporates the Equeue, RPC, and Netclient
libraries, so it now really a big player.

In detail, the following features are available:

 * netstring is about processing strings that occur in network
   context. Features: MIME encoding/decoding, Date/time parsing,
   Character encoding conversion, HTML parsing and printing, URL
   parsing and printing, OO-representation of channels, and a lot
   more.

 * netcgi1 and netcgi2 focus on portable web applications. netcgi1 is
   the older, backward-compatible version, whereas netcgi2 bases on a
   revised design, and is only partly backward-compatible. Supported
   are CGI, FastCGI, AJP (mod_jk), and SCGI.

 * rpc implements ONCRPC (alias SunRPC), the remote procedure call
   technology behind NFS and other Unix services.

 * netplex is a generic server framework. It can be used to build
   stand-alone server programs from individual components like those
   from netcgi2, nethttpd, and rpc.

 * netclient implements clients for HTTP (version 1.1, of course), FTP
   (currently partially), and Telnet.

 * equeue is an event queue used for many protocol implementations. It
   makes it possible to run several clients and/or servers in parallel
   without having to use multi-threading or multi-processing.

 * shell is about calling external commands like a Unix shell does.

 * netshm provides shared memory for IPC purposes.

 * netsys contains bindings for system functions missing in core O'Caml.

 * smtp and pop are two further client implementations for the SMTP
   and POP3 protocols.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       ocaml-pcre-devel

%description devel
This package contains the development files needed to build applications
using %{name}.


%package        nethttpd
Summary:        Ocamlnet HTTP daemon
License:        GPLv2+
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    nethttpd
Nethttpd is a web server component (HTTP server implementation). It
can be used for web applications without using an extra web server, or
for serving web services.


%package        nethttpd-devel
Summary:        Development files for %{name}-nethttpd
License:        GPLv2+
Group:          Development/Other
Requires:       %{name}-nethttpd = %{version}-%{release}

%description    nethttpd-devel
The %{name}-nethttpd-devel package contains libraries and signature
files for developing applications that use %{name}-nethttpd.


%prep
%setup -q -n %{up_name}-%{version}
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build
%define ocamlnet_datadir %{_datadir}/%{name}
# not an autoconf one
./configure \
  -enable-tcl \
  -equeue-tcl-libs -ltcl \
  -bindir %{_bindir} \
  -datadir %{ocamlnet_datadir} \
  -prefer-netcgi2 \
  -with-nethttpd \
  -disable-apache \
  -enable-ssl \
  -enable-gtk2 \
  -with-rpc-auth-dh

# Bletcherous hack to get that extra include path in camlp4 builds.
echo -e '#!/bin/sh\n%{_bindir}/camlp4 -I %{_libdir}/ocaml/camlp4/Camlp4Parsers "$@"' > camlp4; chmod 0755 camlp4; export PATH=`pwd`:$PATH
make all opt


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install \
  OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml" \
  OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml \
  DESTDIR="%{buildroot}"

# cgi/META conflicts with mod_caml
rm -rf %{buildroot}/%{_libdir}/ocaml/cgi

# rpc-generator/dummy.mli is empty and according to Gerd Stolpmann can
# be deleted safely.  This avoids an rpmlint warning.
rm -f %{buildroot}/%{_libdir}/ocaml/rpc-generator/dummy.mli

# Strip libraries.
strip %{buildroot}/%{_libdir}/ocaml/stublibs/*.so


%clean

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE LICENSE.GPL LICENSE.LGPL RELNOTES
%{_libdir}/ocaml/equeue
%{_libdir}/ocaml/equeue-gtk2
%{_libdir}/ocaml/equeue-ssl
%{_libdir}/ocaml/equeue-tcl
#%{_libdir}/ocaml/netcgi1
%{_libdir}/ocaml/netcamlbox
%{_libdir}/ocaml/netcgi2
%{_libdir}/ocaml/netcgi2-plex
%{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netgssapi
%{_libdir}/ocaml/netmulticore
%{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netsys
%{_libdir}/ocaml/pop
%{_libdir}/ocaml/rpc
%{_libdir}/ocaml/rpc-auth-local
%{_libdir}/ocaml/rpc-generator
%{_libdir}/ocaml/rpc-ssl
%{_libdir}/ocaml/smtp
%{_libdir}/ocaml/shell
%{_libdir}/ocaml/rpc-auth-dh
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.o
%exclude %{_libdir}/ocaml/*/*.mli
%{ocamlnet_datadir}
%{_bindir}/netplex-admin
%{_bindir}/ocamlrpcgen

%files devel
%defattr(-,root,root)
%doc doc/html-main
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.o
%{_libdir}/ocaml/*/*.mli
#%exclude %{_libdir}/ocaml/nethttpd-for-netcgi1
%exclude %{_libdir}/ocaml/nethttpd-for-netcgi2
%exclude %{_libdir}/ocaml/nethttpd


%files nethttpd
%defattr(-,root,root)
#%{_libdir}/ocaml/nethttpd-for-netcgi1
%{_libdir}/ocaml/nethttpd-for-netcgi2
%{_libdir}/ocaml/nethttpd
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.mli

%files nethttpd-devel
%defattr(-,root,root)
#%{_libdir}/ocaml/nethttpd-for-netcgi1/*.a
#%{_libdir}/ocaml/nethttpd-for-netcgi1/*.cmxa
#%{_libdir}/ocaml/nethttpd-for-netcgi1/*.mli
%{_libdir}/ocaml/nethttpd/*.a
%{_libdir}/ocaml/nethttpd/*.cmxa
%{_libdir}/ocaml/nethttpd/*.mli



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 2.2.9-10
+ Revision: 797777
- Rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - relink against libpcre.so.1

* Mon Sep 14 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-8mdv2011.0
+ Revision: 440706
- rebuild

* Wed Sep 09 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-7mdv2010.0
+ Revision: 436141
- added support for cryptgps
- the devel package requires ocaml-pcre-devel

* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-6mdv2010.0
+ Revision: 419709
- incremented mkrel
- corrected the split

* Mon Aug 10 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-5mdv2010.0
+ Revision: 413869
- incremented mkrel
- corrected Requires

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-4mdv2010.0
+ Revision: 390090
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-3mdv2010.0
+ Revision: 385257
- pcre dep updated

* Sun Jan 11 2009 Florent Monnier <blue_prawn@mandriva.org> 2.2.9-2mdv2009.1
+ Revision: 328195
- corrected group
- build/install all the modules
- update the home page
- a more detailed description
- imported a patch from fedora
  (modifications made with the help of the fedora's spec made by Richard W.M. Jones)

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-1mdv2009.1
+ Revision: 320723
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-1mdv2009.0
+ Revision: 272354
- fix build with latest glibc
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-4mdv2008.1
+ Revision: 181156
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-3mdv2008.0
+ Revision: 78371
- move stup libs into non-devel package

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-2mdv2008.0
+ Revision: 77685
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Thu Jun 07 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.2.7-1mdv2008.0
+ Revision: 36815
- new release: 2.2.7


