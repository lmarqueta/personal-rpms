Name:		task
Version:	2.6.2
Release:	1%{?dist}.personal
Summary:	taskwarrior manages your TODO list from the command line
License:	MIT
URL:		https://taskwarrior.org/
Source0:	%{url}/download/%{name}-%{version}.tar.gz

BuildRequires: 	cmake 
BuildRequires: 	gnutls-devel 
BuildRequires: 	libuuid-devel

# do not build debug info
%global debug_package %{nil}

%description
Taskwarrior is Free and Open Source Software that manages your TODO list from
the command line. It is flexible, fast, and unobtrusive. It does its job then
gets out of your way.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=release .
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc /usr/share/doc/task/*
%{_bindir}/%{name}
/usr/share/man/*
/usr/share/zsh/site-functions/_task

%changelog
* Wed Sep 13 2023 Luis Marqueta <luis@marqueta.org> 2.6.2-1
- Initial package for RHEL 9
