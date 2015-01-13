# http://ros.org/doc/groovy/api/catkin/html/user_guide/supposed.html
cmake_minimum_required(VERSION 2.8.3)
project(jskeus)

find_package(euslisp REQUIRED)
message(STATUS "ARCHDIR=${ARCHDIR}")
message(STATUS "EUSDIR=${EUSDIR}")

# build irteus on install command
set(INSTALLDIR ${CMAKE_INSTALL_PREFIX}/share/euslisp/jskeus/eus/)
add_custom_command(OUTPUT ${INSTALLDIR}
  COMMAND cmake -E make_directory ${INSTALLDIR}/${ARCHDIR}/bin
  COMMAND cmake -E make_directory ${INSTALLDIR}/${ARCHDIR}/obj
  COMMAND cmake -E make_directory ${INSTALLDIR}/${ARCHDIR}/lib)
add_custom_target(compile_jskeus
  DEPENDS ${INSTALLDIR}
  COMMAND export EUSDIR=${EUSDIR} lt_cv_sys_lib_dlsearch_path_spec=${lt_cv_sys_lib_dlsearch_path_spec} && \$\(MAKE\) -j1 -l1 -C ${PROJECT_SOURCE_DIR}/irteus -f Makefile ARCHDIR=${ARCHDIR} EUSDIR=${EUSDIR} IRTEUSDIR=\${DESTDIR}${INSTALLDIR})
install(CODE "execute_process(COMMAND \"${CMAKE_COMMAND}\" --build \"${CMAKE_BINARY_DIR}\" --target compile_jskeus)")

install(DIRECTORY doc
   DESTINATION share/jskeus/
   USE_SOURCE_PERMISSIONS)
install(DIRECTORY irteus
   DESTINATION share/euslisp/jskeus/
   USE_SOURCE_PERMISSIONS)
install(FILES package.xml DESTINATION share/jskeus/)





