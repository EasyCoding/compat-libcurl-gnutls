%undefine __brp_ldconfig

%global debug_package %{nil}
%global libname libcurl-gnutls.so.4

%if 0%{?__isa_bits} == 64
%define libsuffix (%{?__isa_bits}bit)
%else
%define libsuffix %{nil}
%endif

Name: compat-libcurl-gnutls
Version: 1.0
Release: 2%{?dist}

URL: https://github.com/EasyCoding/%{name}
Summary: Libcurl-gnutls compatibility library
License: GPLv3+

BuildRequires: libcurl
Requires: libcurl%{?_isa}

Provides: %{libname}%{?_isa}
Provides: %{libname}()%{libsuffix}
Provides: %{libname}(CURL_GNUTLS_3)%{libsuffix}

%description
Provides libcurl-gnutls compatibility library for different 3rdparty
applications.

%prep
%setup -q -c -T

%build
# Nothing to build...

%install
mkdir -p "%{buildroot}%{_libdir}"
ln -s %{_libdir}/libcurl.so.4 "%{buildroot}%{_libdir}/%{libname}"

%ldconfig_scriptlets

%files
%{_libdir}/%{libname}

%changelog
* Thu May 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-2
- Fixed build under Fedora 28+.
- Resolved new issues with GitKraken.

* Mon Apr 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Initial release.
