Name:           ros-indigo-cob-command-gui
Version:        0.6.6
Release:        0%{?dist}
Summary:        ROS cob_command_gui package

Group:          Development/Libraries
License:        LGPL
URL:            http://www.ros.org/wiki/cob_command_gui
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz-python
Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-script-server
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
BuildRequires:  ros-indigo-catkin

%description
This package provides a simple GUI for operating Care-O-bot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jul 17 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

* Mon Jul 17 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.5-1
- Autogenerated by Bloom

* Mon Oct 10 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.5-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

