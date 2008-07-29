%define up_name	ocamlnet
%define name	ocaml-%{up_name}
%define version	2.2.7
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml internet protocols and conventions
Source: 	http://downloads.sourceforge.net/ocamlnet/%{up_name}-%{version}.tar.gz
Patch0:		%{name}-2.2.4-destdir.patch
Patch1:		%{name}-2.2.4-fix-shm-test.patch
URL:		http://ocamlnet.sourceforge.net/
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

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE LICENSE.GPL LICENSE.LGPL RELNOTES
%doc doc/html-main
%dir %{ocaml_sitelib}/equeue
%{ocaml_sitelib}/equeue/*.cmi
%dir %{ocaml_sitelib}/netcgi1
%{ocaml_sitelib}/netcgi1/*.cmi
%dir %{ocaml_sitelib}/netcgi2
%{ocaml_sitelib}/netcgi2/*.cmi
%dir %{ocaml_sitelib}/netcgi2-plex
%{ocaml_sitelib}/netcgi2-plex/*.cmi
%dir %{ocaml_sitelib}/netclient
%{ocaml_sitelib}/netclient/*.cmi
%dir %{ocaml_sitelib}/netplex
%{ocaml_sitelib}/netplex/*.cmi
%dir %{ocaml_sitelib}/netshm
%{ocaml_sitelib}/netshm/*.cmi
%dir %{ocaml_sitelib}/netstring
%{ocaml_sitelib}/netstring/*.cmi
%dir %{ocaml_sitelib}/netsys
%{ocaml_sitelib}/netsys/*.cmi
%dir %{ocaml_sitelib}/pop
%{ocaml_sitelib}/pop/*.cmi
%dir %{ocaml_sitelib}/rpc
%{ocaml_sitelib}/rpc/*.cmi
%dir %{ocaml_sitelib}/rpc-auth-local
%{ocaml_sitelib}/rpc-auth-local/*.cmi
%dir %{ocaml_sitelib}/rpc-generator
%{ocaml_sitelib}/rpc-generator/*.cmi
%dir %{ocaml_sitelib}/smtp
%{ocaml_sitelib}/smtp/*.cmi
%dir %{ocaml_sitelib}/shell
%{ocaml_sitelib}/shell/*.cmi
%{ocaml_sitelib}/stublibs/*

%files devel
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/ocamlnet
%{ocaml_sitelib}/cgi
%{ocaml_sitelib}/equeue/*
%exclude %{ocaml_sitelib}/equeue/*.cmi
%{ocaml_sitelib}/netcgi1/*
%exclude %{ocaml_sitelib}/netcgi1/*.cmi
%{ocaml_sitelib}/netcgi2/*
%exclude %{ocaml_sitelib}/netcgi2/*.cmi
%{ocaml_sitelib}/netcgi2-plex/*
%exclude %{ocaml_sitelib}/netcgi2-plex/*.cmi
%{ocaml_sitelib}/netclient/*
%exclude %{ocaml_sitelib}/netclient/*.cmi
%{ocaml_sitelib}/netplex/*
%exclude %{ocaml_sitelib}/netplex/*.cmi
%{ocaml_sitelib}/netshm/*
%exclude %{ocaml_sitelib}/netshm/*.cmi
%{ocaml_sitelib}/netstring/*
%exclude %{ocaml_sitelib}/netstring/*.cmi
%{ocaml_sitelib}/netsys/*
%exclude %{ocaml_sitelib}/netsys/*.cmi
%{ocaml_sitelib}/pop/*
%exclude %{ocaml_sitelib}/pop/*.cmi
%{ocaml_sitelib}/rpc/*
%exclude %{ocaml_sitelib}/rpc/*.cmi
%{ocaml_sitelib}/rpc-auth-local/*
%exclude %{ocaml_sitelib}/rpc-auth-local/*.cmi
%{ocaml_sitelib}/rpc-generator/*
%exclude %{ocaml_sitelib}/rpc-generator/*.cmi
%{ocaml_sitelib}/smtp/*
%exclude %{ocaml_sitelib}/smtp/*.cmi
%{ocaml_sitelib}/shell/*
%exclude %{ocaml_sitelib}/shell/*.cmi
