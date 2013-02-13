%define gitref     00370b5

Name:		kcm_touchpad
Version:	0.3.1
Summary:	Touchpad Configuration GUI for KDE
Release:	11
License:	GPL
Group:		Graphical desktop/KDE
URL:		http://kde-apps.org/content/show.php/kcm_touchpad?content=113335
Source0:	http://download.github.com/mishaaq-%name-%gitref.tar.gz
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
BuildRequires:	x11-driver-input-synaptics-devel
BuildRequires:	pkgconfig(xi)

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
%setup -q -n mishaaq-%{name}-%{gitref}
%apply_patches

%build
%cmake_kde4

%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_docdir}/%{name}/*

%find_lang %{name}

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-8mdv2011.0
+ Revision: 666006
- mass rebuild

* Thu Sep 09 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-7mdv2011.0
+ Revision: 576997
- patch110: fix system settings category for KDE 4.6

* Mon May 24 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-6mdv2010.1
+ Revision: 545818
- patch109: add translations from Mandriva SVN

* Tue Mar 09 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-5mdv2010.1
+ Revision: 517167
- patch108: fix ksyndaemon not terminated on logout

* Sat Feb 13 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-4mdv2010.1
+ Revision: 505581
- patch106, patch107: implement SmartMode based on syndaemon

* Sat Jan 23 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-3mdv2010.1
+ Revision: 495185
- patch104: better checking of touchpad capabilities

* Wed Jan 20 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-2mdv2010.1
+ Revision: 494089
- patch103: do not disable scrolling when sensitivity set to High

* Tue Jan 12 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 490355
- remove patch102 - integrated upstream
- new version

* Thu Nov 12 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.0-3mdv2010.1
+ Revision: 465391
- fix setting of coasting speed on startup (again)

* Thu Nov 12 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.0-2mdv2010.1
+ Revision: 465132
- rebuild with new Qt

* Sat Nov 07 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 462365
- update snapshot to official release
- use "official" home page for URL

* Sun Oct 25 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.95-2mdv2010.0
+ Revision: 459235
- new GIT snapshot - fix CoastingSpeed restore on KDE startup
- new GIT snapshot - fix buttons sometimes disabed on startup

* Fri Oct 23 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2.95-0.1mdv2010.0
+ Revision: 459056
- properly package translation files
- disable patch0 - seems to build fine without it
- remove patch101 - modified version upstream
- remove patch100 - integrated upstream
- new GIT snapshot - post 0.2.95

* Sat Oct 17 2009 Andrey Borzenkov <arvidjaar@mandriva.org> 0.2-0.3mdv2010.0
+ Revision: 458037
- patch101: fix saving/restoring of CoastingSpeed
- patch100: fix setting of boolean properties on startup. Most notably it broke tapping

  + Colin Guthrie <cguthrie@mandriva.org>
    - New upstream snapshot

* Fri Oct 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2-0.1mdv2010.0
+ Revision: 457821
- Fix minimum requires

  + Colin Guthrie <cguthrie@mandriva.org>
    - import kcm_touchpad

