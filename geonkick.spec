%global debug_package %{nil}
Name:           geonkick
Version:        1.9.2
Release:        1%{?dist}
Summary:        A synthesizer that can synthesize elements of percussion

License:        GPLv3+
URL:            https://gitlab.com/geontime/geonkick
Source0:        https://gitlab.com/geontime/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

Patch0:         geonkick-1.9.2-lv2-install-dir-fix.patch

BuildRequires:  cmake
BuildRequires:  libsndfile-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  lv2-devel
BuildRequires:  rapidjson-devel
BuildRequires:  libX11-devel
BuildRequires:  cairo-devel
BuildRequires:  redkite-devel

%global common_desc \
Geonkick is a synthesizer that can synthesize elements of percussion. The most\
basic examples are kicks, snares, hit-hats, shakers, claps and sticks. Also, it\
can play samples.

%description
%common_desc

%package -n lv2-%{name}-plugins
Summary:        Geonkick plugin in LV2 format

%description -n lv2-%{name}-plugins
%common_desc

This package contains the LV2 plugin.

%prep
%autosetup -p1 -n %{name}-v%{version} 

%build
mkdir build
cd build
%cmake -DGKICK_REDKITE_SDK_PATH=/usr -DENABLE_STANDALONE=true ../
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/mime/packages/%{name}.xml

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Fri Jan 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 1.9.2-1
- Initial build
