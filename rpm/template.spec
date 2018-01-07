Name:           ros-kinetic-cob-script-server
Version:        0.6.7
Release:        0%{?dist}
Summary:        ROS cob_script_server package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/cob_script_server
Source0:        %{name}-%{version}.tar.gz

Requires:       graphviz-python
Requires:       python-ipython
Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-cob-light
Requires:       ros-kinetic-cob-mimic
Requires:       ros-kinetic-cob-sound
Requires:       ros-kinetic-control-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-move-base-msgs
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-trajectory-msgs
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-trajectory-msgs

%description
The cob_script_server package provides a simple interface to operate Care-O-bot.
It can be used via the python API or the actionlib interface.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Jan 07 2018 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.7-0
- Autogenerated by Bloom

* Tue Jul 25 2017 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.6-0
- Autogenerated by Bloom

