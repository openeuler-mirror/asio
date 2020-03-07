%global debug_package %{nil}
%global commit 28d9b8d6df708024af5227c551673fdb2519f5bf

Name:           asio
Version:        1.10.8
Release:        9
Summary:        A cross-platform C++ library for network programming

Group:          System Environment/Libraries
License:        Boost
URL:            https://think-async.com/Asio
Source0:        https://github.com/chriskohlhoff/asio/archive/28d9b8d6df708024af5227c551673fdb2519f5bf.tar.gz

BuildRequires:  gcc-c++ autoconf automake openssl-devel boost-devel perl-generators

%description
Asio is a cross-platform C++ library for network and low-level I/O programming
that provides developers with a consistent asynchronous I/O model using a
modern C++ approach.

%package devel
Summary:        Provides header files for asio
Requires:       openssl-devel boost-devel

%description devel
Asio is a cross-platform C++ library for network and low-level I/O
programming. And this package provides header files for developer
to develop applications with asio.

%prep
%autosetup -n asio-28d9b8d6df708024af5227c551673fdb2519f5bf/asio -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files devel
%doc src/doc/*
%license LICENSE_1_0.txt
%{_includedir}/asio/
%{_includedir}/asio.hpp

%changelog
* Thu Mar 05 2020 sunguoshuai <sunguoshuai@huawei.com> - 1.10.8-9
- Package init.
