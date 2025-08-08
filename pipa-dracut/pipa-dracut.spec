Name: pipa-dracut
Version: 1.1
Release: 1
Summary: Dracut modules for the Xiaomi Pad 6
Source1: module-setup.sh
License: GPL2.0

Requires: xiaomi-pipa-firmware

%description
Dracut modules for the Xiaomi Pad 6

%install
install -Dm755 %{SOURCE1} %{buildroot}/usr/lib/dracut/modules.d/90nvtfw/module-setup.sh

%files
/usr/lib/dracut/modules.d/90nvtfw/*
