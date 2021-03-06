# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate block-cipher-trait

Name:           rust-%{crate}
Version:        0.6.2
Release:        3%{?dist}
Summary:        Traits for description of block ciphers

# Upstream license specification: MIT OR Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/block-cipher-trait
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(generic-array/default) >= 0.12.0 with crate(generic-array/default) < 0.13.0)

%global _description \
Traits for description of block ciphers.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+blobby-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blobby-devel %{_description}

This package contains library source intended for building other packages
which use "blobby" feature of "%{crate}" crate.

%files       -n %{name}+blobby-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+dev-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev-devel %{_description}

This package contains library source intended for building other packages
which use "dev" feature of "%{crate}" crate.

%files       -n %{name}+dev-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 18:35:46 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6.2-1
- Initial package
