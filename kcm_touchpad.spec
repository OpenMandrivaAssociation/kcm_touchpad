%define gitref     00370b5

Summary:	Touchpad Configuration GUI for KDE
Name:		kcm_touchpad
Version:	0.3.1
Release:	12
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		http://kde-apps.org/content/show.php/kcm_touchpad?content=113335
Source0:	http://download.github.com/mishaaq-%{name}-%{gitref}f.tar.gz
#Patch0:         synaptic-1.1.3.patch

# Upstream patches
#
# (bor) fix setting of boolean properties on startup
# Patch100:	fix_boolean_properties_on_startup.patch
# (bor) fix saving/restoring of CoastingSpeed state
# Patch101:	fix_scroll_coasting.patch
# (bor) fix saving/restoring of CoastingSpeed state again
# Patch102:	0001-Fix-settings-of-coasting-speed-on-startup.patch
# (bor) fix setting scrolling sensitivity to High disables scrolling
Patch103:	0001-fix-the-scrolling-being-disabled-after-setting-the-s.patch
# (bor) better checking of supported touchpad capabilities
Patch104:	0002-Add-support-for-querying-touchpad-capabilities.patch
Patch105:	0003-Do-not-offer-for-configuration-actions-that-touchpad.patch
# (bor) implement SmartMode
Patch106:	0004-Add-ksyndaemon-daemon-to-monitor-touchpad.patch
Patch107:	0005-Implement-SmartMode-as-interface-to-ksyndaemon.patch
# (bor) fix previous patch
Patch108:	0006-ksyndaemon-was-not-terminated-on-session-logout.patch
# (bor) add translations from Mandriva SVN
Patch109:	0007-Add-l10n-files-from-Mandriva-cooker.patch
# (bor) fix system settings category for KDE 4.6
Patch110:	0008-Fix-System-Settings-category-for-4.6.patch
Patch111:       touchpad.desktop-localization.patch

BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xorg-synaptics)
Requires:	kdebase4-runtime

%description
Touchpad Configuration GUI for KDE.

%files -f %{name}.lang
%doc AUTHORS README
%{_kde_libdir}/kde4/kcm_touchpad.so
%{_kde_libdir}/kde4/libexec/ksyndaemon
%{_kde_services}/touchpad.desktop
%{_kde_services}/ksyndaemon.desktop
%{_datadir}/dbus-1/services/org.kde.ksyndaemon.service

#-----------------------------------------------------------------------------

%prep
%setup -qn mishaaq-%{name}-%{gitref}
%apply_patches

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_docdir}/%{name}/*

%find_lang %{name}

