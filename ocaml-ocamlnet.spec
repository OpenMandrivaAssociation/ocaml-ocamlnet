%define up_name	ocamlnet
%define name	ocaml-%{up_name}
%define version	2.2.9
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml internet protocols and conventions
License:	GPL
Group:		Development/Other
URL:		http://ocamlnet.sourceforge.net/
Source: 	http://downloads.sourceforge.net/ocamlnet/%{up_name}-%{version}.tar.gz
Patch0:		%{name}-2.2.4-destdir.patch
Patch1:		%{name}-2.2.4-fix-shm-test.patch
Patch2:		%{name}-2.2.9-fix-build.patch
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A collection of modules for the Objective Caml language which focus on
application-level Internet protocols and conventions.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	ocaml-pcre-devel
Requires:	ncurses-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build
./configure -datadir %{_datadir}/ocamlnet # not an autoconf one
make all opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml" DESTDIR="%{buildroot}"
rm -f %{buildroot}/%{_libdir}/ocaml/stublibs/*.so.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE LICENSE.GPL LICENSE.LGPL RELNOTES
%doc doc/html-main
%{_bindir}/*
%{_datadir}/ocamlnet
%{_libdir}/ocaml/cgi
%{_libdir}/ocaml/equeue
%{_libdir}/ocaml/netcgi1
%{_libdir}/ocaml/netcgi2
%{_libdir}/ocaml/netcgi2-plex
%{_libdir}/ocaml/netclient
%{_libdir}/ocaml/netplex
%{_libdir}/ocaml/netshm
%{_libdir}/ocaml/netstring
%{_libdir}/ocaml/netsys
%{_libdir}/ocaml/pop
%{_libdir}/ocaml/rpc
%{_libdir}/ocaml/rpc-auth-local
%{_libdir}/ocaml/rpc-generator
%{_libdir}/ocaml/smtp
%{_libdir}/ocaml/shell
%{_libdir}/ocaml/stublibs/*.so
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.cmx
%exclude %{_libdir}/ocaml/*/*.o
%exclude %{_libdir}/ocaml/*/*.mli


%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.o
%{_libdir}/ocaml/*/*.mli
