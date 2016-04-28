
cmake_minimum_required(VERSION 2.6)

project(CALIB3D)

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_BINARY_DIR})

include_directories(/opt/local/include)
link_directories(/opt/local/lib)
include(FindPkgConfig)
pkg_search_module(OPENCV REQUIRED opencv>=2.3)
include_directories(${OPENCV_INCLUDE_DIRS})

set(CMAKE_C_FLAGS "-Wall -g")
set(CMAKE_CXX_FLAGS "-Wall -g")

if (APPLE OR UNIX)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wsign-compare -frounding-math")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wsign-compare -frounding-math")
endif()

if (TRUE)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mcpu=cortex-a7 -mfpu=neon-vfpv4 -mfloat-abi=hard")
endif()

set(CMAKE_C_FLAGS_DEBUG "-O")
set(CMAKE_CXX_FLAGS_DEBUG "-O")

set(CMAKE_C_FLAGS_RELEASE "-O2")
set(CMAKE_CXX_FLAGS_RELEASE "-O2")

add_subdirectory(src)

