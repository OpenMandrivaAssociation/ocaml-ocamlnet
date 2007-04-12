%define up_name	ocamlnet
%define name	ocaml-%{up_name}
%define version	2.2.4
%define release	%mkrel 5
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml internet protocols and conventions
Source: 	http://downloads.sourceforge.net/ocamlnet/%{up_name}-%{version}.tar.bz2
Patch0:     %{name}-2.2.4-destdir.patch
Patch1:     %{name}-2.2.4-fix-shm-test.patch
URL:		http://ocamlnet.sourceforge.net
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  findlib
BuildRequires:  ocaml-pcre-devel
BuildRequires:  ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A collection of modules for the Objective Caml language which focus on
application-level Internet protocols and conventions.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   ocaml-pcre-devel
Requires:   ncurses-devel

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch0 -p 1
%patch1 -p 1

%build
./configure -datadir %{_datadir}/ocamlnet # not an autoconf one
make all opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}" DESTDIR="%{buildroot}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.so.owner

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE LICENSE.GPL LICENSE.LGPL RELNOTES
%doc doc/html-main
%{_bindir}/*
%{_datadir}/ocamlnet
%{ocaml_sitelib}/cgi
%{ocaml_sitelib}/equeue
%{ocaml_sitelib}/netcgi1
%{ocaml_sitelib}/netcgi2
%{ocaml_sitelib}/netcgi2-plex
%{ocaml_sitelib}/netclient
%{ocaml_sitelib}/netplex
%{ocaml_sitelib}/netshm
%{ocaml_sitelib}/netstring
%{ocaml_sitelib}/netsys
%{ocaml_sitelib}/pop
%{ocaml_sitelib}/rpc
%{ocaml_sitelib}/rpc-auth-local
%{ocaml_sitelib}/rpc-generator
%{ocaml_sitelib}/smtp
%{ocaml_sitelib}/shell
%{ocaml_sitelib}/stublibs/*


