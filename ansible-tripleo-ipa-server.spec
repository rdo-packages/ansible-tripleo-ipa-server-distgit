
%global srcname ansible_tripleo_ipa_server
%global rolename ansible-tripleo-ipa-server

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           %{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible assets for configuring the FreeIPA server for TripleO.

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://opendev.org/x/ansible-tripleo-ipa-server/
Source0:        https://tarballs.opendev.org/x/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr

Requires: ansible-freeipa
Requires: krb5-workstation

%description

Ansible assets for configuring the FreeIPA server for TripleO.

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_install}


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/


%changelog
