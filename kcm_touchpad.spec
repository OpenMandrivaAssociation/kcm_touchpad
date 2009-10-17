%define gitref     2bb4e58
Name:           kcm_touchpad
Version:        0.2
Summary:        Touchpad Configuration GUI for KDE
Release:        %mkrel 0.3
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://github.com/mishaaq/kcm_touchpad
Source0:        mishaaq-%name-%gitref.tar.gz
Patch0:         synaptic-1.1.3.patch

# (bor) fix setting of boolean properties on startup
Patch100:	fix_boolean_properties_on_startup.patch

BuildRoot:      %_tmppath/%name-%version-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  x11-driver-input-synaptics-devel

Requires:       kdebase4-runtime

%description
Touchpad Configuration GUI for KDE

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_kde_libdir}/kde4/kcm_touchpad.so
%{_kde_datadir}/kde4/services/touchpad.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n mishaaq-%name-%gitref
%apply_patches

%build

%cmake_kde4

%make


%install
rm -rf %buildroot
%makeinstall_std -C build

rm -f %{buildroot}%{_docdir}/%{name}/*

%clean
rm -rf %{buildroot}

