# Catkin User Guide: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/user_guide.html
# Catkin CMake Standard: http://www.ros.org/doc/groovy/api/catkin/html/user_guide/standards.html
cmake_minimum_required(VERSION 2.8.3)
project(pointcloud_publisher)
# Load catkin and all dependencies required for this package
# TODO: remove all from COMPONENTS that are not catkin packages.
find_package(catkin REQUIRED COMPONENTS laser_geometry roscpp sensor_msgs message_runtime std_msgs message_generation rospy laser_tf_py tf pcl_ros)
# CATKIN_MIGRATION: removed during catkin migration
# cmake_minimum_required(VERSION 2.4.6)

# CATKIN_MIGRATION: removed during catkin migration
# include($ENV{ROS_ROOT}/core/rosbuild/rosbuild.cmake)

# Set the build type.  Options are:
#  Coverage       : w/ debug symbols, w/o optimization, w/ code-coverage
#  Debug          : w/ debug symbols, w/o optimization
#  Release        : w/o debug symbols, w/ optimization
#  RelWithDebInfo : w/ debug symbols, w/ optimization
#  MinSizeRel     : w/o debug symbols, w/ optimization, stripped binaries
#set(ROS_BUILD_TYPE RelWithDebInfo)


# CATKIN_MIGRATION: removed during catkin migration
# rosbuild_init()

#set the default path for built executables to the "bin" directory

# CATKIN_MIGRATION: removed during catkin migration
# set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory

# CATKIN_MIGRATION: removed during catkin migration
# set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

#uncomment if you have defined messages
#rosbuild_genmsg()
#uncomment if you have defined services
add_service_files(
  FILES
  SavePCLData.srv
)
## Generate added messages and services with any dependencies listed here
generate_messages(
    DEPENDENCIES 
)

# catkin_package parameters: http://ros.org/doc/groovy/api/catkin/html/dev_guide/generated_cmake_api.html#catkin-package
# TODO: fill in what other packages will need to use this package
catkin_package(
    DEPENDS  # TODO
    CATKIN_DEPENDS laser_geometry roscpp sensor_msgs message_runtime std_msgs message_generation rospy laser_tf_py tf pcl_ros
    INCLUDE_DIRS # TODO include
    LIBRARIES # TODO
)

include_directories( ${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS})


#common commands for building c++ executables and libraries
#rosbuild_add_library(${PROJECT_NAME} src/example.cpp)
#target_link_libraries(${PROJECT_NAME} another_library)

# CATKIN_MIGRATION: removed during catkin migration
# rosbuild_add_boost_directories()
#rosbuild_link_boost(${PROJECT_NAME} thread)
#rosbuild_add_executable(example examples/example.cpp)
#target_link_libraries(example ${PROJECT_NAME})

add_executable(pointcloud_publisher src/pointcloud_publisher.cpp)
target_link_libraries(pointcloud_publisher ${catkin_LIBRARIES})
add_dependencies(pointcloud_publisher ${catkin_EXPORTED_TARGETS})
add_dependencies(pointcloud_publisher ${PROJECT_NAME}_generate_messages_cpp)
add_executable(pointcloud_converter src/pointcloud_converter.cpp)
target_link_libraries(pointcloud_converter ${catkin_LIBRARIES})
add_dependencies(pointcloud_converter ${catkin_EXPORTED_TARGETS})
add_dependencies(pointcloud_converter ${PROJECT_NAME}_generate_messages_cpp)

find_package(Boost REQUIRED COMPONENTS signals)
include_directories(${Boost_INCLUDE_DIRS})
target_link_libraries(pointcloud_publisher ${Boost_LIBRARIES})

