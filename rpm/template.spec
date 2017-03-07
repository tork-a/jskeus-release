Name:           ros-indigo-jskeus
Version:        1.1.0
Release:        0%{?dist}
Summary:        ROS jskeus package

Group:          Development/Libraries
License:        BSD
URL:            http://euslisp.github.io/jskeus/manual.html
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-euslisp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-euslisp

%description
EusLisp software developed and used by JSK at The University of Tokyo

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
* Tue Mar 07 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.0-0
- Autogenerated by Bloom

* Fri Dec 30 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.14-0
- Autogenerated by Bloom

* Wed Aug 03 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.13-1
- Autogenerated by Bloom

* Tue Aug 02 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.13-0
- Autogenerated by Bloom

* Sun Mar 20 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.12-0
- Autogenerated by Bloom

* Mon Nov 02 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.11-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.10-0
- Autogenerated by Bloom

* Thu Jul 09 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.9-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.8-0
- Autogenerated by Bloom

* Thu Apr 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.6-0
- Autogenerated by Bloom

* Wed Apr 22 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.5-0
- Autogenerated by Bloom

* Fri Mar 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.4-1
- Autogenerated by Bloom

* Fri Mar 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.4-0
- Autogenerated by Bloom

* Sun Feb 22 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.3-0
- Autogenerated by Bloom

* Fri Feb 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-5
- Autogenerated by Bloom

* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-4
- Autogenerated by Bloom

* Tue Jan 20 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-3
- Autogenerated by Bloom

* Thu Jan 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-2
- Autogenerated by Bloom

* Wed Jan 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-1
- Autogenerated by Bloom

* Tue Jan 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.2-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.1-1
- Autogenerated by Bloom

* Mon Dec 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.1-0
- Autogenerated by Bloom

