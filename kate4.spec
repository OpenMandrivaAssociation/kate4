## We currently only build/ship -part
## Other bits are replaced by kf5 kate-14.12+

Name:    kate4
Summary: Advanced Text Editor for KDE4
Version: 4.14.3
Release: 1
Group:	Graphical desktop/KDE
# kwrite LGPLv2+
# kate: app LGPLv2, plugins, LGPLv2 and LGPLv2+ and GPLv2+
# ktexteditor: LGPLv2
# katepart: LGPLv2
License: LGPLv2 and LGPLv2+ and GPLv2+
URL:     https://projects.kde.org/projects/kde/applications/kate
Source0: http://download.kde.org/stable/%{version}/src/kate-%{version}.tar.xz

BuildRequires: kdelibs4-devel >= 4.14

%description
%{summary}.

%package -n katepart4
Summary: KDE4 Kate kpart plugin
License: LGPLv2
Provides:  kate4-part = %{version}-%{release}

%description -n katepart4
%{summary}, needed by some KDE4 applications.


%prep
%setup -q -n kate-%{version}


%build
%{cmake_kde4} ..

make %{?_smp_mflags} -C part
make %{?_smp_mflags} -C addons/ktexteditor


%install
make install/fast DESTDIR=%{buildroot} -C build/part
make install/fast DESTDIR=%{buildroot} -C build/addons/ktexteditor

## unpackaged files
rm -fv %{buildroot}%{_kde_libdir}/libkatepartinterfaces.so

%files -n katepart4
%doc COPYING.LIB
%doc part/INDENTATION part/README*
%{_kde_libdir}/kde4/katepart.so
%{_kde_libdir}/kde4/ktexteditor_*.so
%{_kde_libdir}/libkatepartinterfaces.so.4*
%{_kde_appsdir}/katepart/
%{_kde_appsdir}/ktexteditor_*/
%{_kde_configdir}/katemoderc
%{_kde_configdir}/kateschemarc
%{_kde_configdir}/katesyntaxhighlightingrc
%{_kde_configdir}/ktexteditor_codesnippets_core.knsrc
%{_kde_datadir}/kde4/services/katepart.desktop
%{_kde_datadir}/kde4/services/ktexteditor_*.desktop
%{_kde_iconsdir}/hicolor/*/apps/ktexteditor*


