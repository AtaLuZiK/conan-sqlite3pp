cmake_minimum_required(VERSION 3.2)
project(sqlite3pp
  VERSION 1.0.8
  LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set (CMAKE_CXX_STANDARD 11)

set(SQLITE3PP_SOURCES
  sqlite3pp/src/sqlite3pp.h
  sqlite3pp/src/sqlite3pp.cpp
  sqlite3pp/src/sqlite3ppext.h
  sqlite3pp/src/sqlite3ppext.cpp
)

add_library(sqlite3pp STATIC ${SQLITE3PP_SOURCES})
