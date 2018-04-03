%global debug_package %{nil}
%global libname libcurl-gnutls.so.4

Name: compat-libcurl-gnutls
Version: 1.0
Release: 1%{?dist}

URL: https://github.com/EasyCoding/%{name}
Summary: Libcurl-gnutls compatibility library
License: GPLv3+

BuildRequires: libcurl-devel
Requires: libcurl%{?_isa}

%description
Provides libcurl-gnutls compatibility library for different 3rdparty
applications.

%prep
%setup -q -c -T

%build
# Nothing to build...

%install
mkdir -p "%{buildroot}%{_libdir}"
ln -s %{_libdir}/libcurl.so.4.4.0 "%{buildroot}%{_libdir}/%{libname}"

%ldconfig_scriptlets

%files
%{_libdir}/%{libname}

%changelog
* Mon Apr 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Initial release.
