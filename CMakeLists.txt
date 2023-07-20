#setting the project variables
set(TARGET_EXECUTABLE_NAME "demo_app")
set(HEADERS_DIRECTORY "include")
set(SOURCES_DIRECTORY "src")
set(PROTO_DIRECTORY "proto")
set(CMAKE_CXX_STANDARD 17)
###########################################


cmake_minimum_required(VERSION 3.9)
project("demoApp_example.exe" VERSION 1.0.0)
##########################################


##########################################
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
##########################################

##########################################
# find the protobuf compiler and libraries
find_package(Protobuf REQUIRED)

##########################################

file(GLOB_RECURSE SOURCES "${SOURCES_DIRECTORY}/*.cpp")
file(GLOB_RECURSE HEADERS "${HEADERS_DIRECTORY}/*.hpp")
file(GLOB_RECURSE PROTO_SOURCES "${PROTO_DIRECTORY}/*.proto")

##########################################

PROTOBUF_GENERATE_CPP(PROTO_SRCS PROTO_HDRS ${PROTO_SOURCES})

##########################################

include_directories(${HEADERS_DIRECTORY} PUBLIC ${PROTOBUF_INCLUDE_DIRS} ${CMAKE_CURRENT_BINARY_DIR})

add_executable(${TARGET_EXECUTABLE_NAME} ${SOURCES} ${PROTO_SRCS} ${PROTO_HDRS})

target_link_libraries(${TARGET_EXECUTABLE_NAME} ${CONAN_LIBS})