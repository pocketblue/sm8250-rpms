%global _firmwarepath /usr/lib/firmware
%global _hexegonpath /usr/share/qcom/sm8250/Xiaomi/pipa
%global __requires_exclude ^.*\\.so.*$

Name: xiaomi-pipa-firmware
Version: 1.0
Release: 2
Summary: Firmware package for xiaomi-pipa
Source1: %{name}-%{version}.tar.gz
License: Unknown

Requires: qcom-firmware

%description
Firmware for various compoents in Xiaomi Mi Pad 6 including 
touchscreen, SoC.

%prep
tar -xzf %{SOURCE1}

%install
cp -r src/* %{buildroot}

%files
%{_firmwarepath}/qcom/*
%{_firmwarepath}/novatek/*
%{_firmwarepath}/awinic/*
%{_hexegonpath}/*
