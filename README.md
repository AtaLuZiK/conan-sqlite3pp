# conan-sqlite3pp

Conan package for [SQLite3++](https://github.com/iwongu/sqlite3pp)

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/conan-community).

## Package Status

| Bintray | Travis | Appveyor |
|---------|--------|----------|
|[ ![Download](https://api.bintray.com/packages/zimmerk/conan/sqlite3pp%3Azimmerk/images/download.svg) ](https://bintray.com/zimmerk/conan/sqlite3pp%3Azimmerk/_latestVersion)|[![Build Status](https://travis-ci.org/AtaLuZiK/conan-sqlite3pp.svg?branch=release%2F1.0.8)](https://travis-ci.org/AtaLuZiK/conan-sqlite3pp)|[![Build status](https://ci.appveyor.com/api/projects/status/wqcslta857jkhni7/branch/release/1.0.8?svg=true)](https://ci.appveyor.com/project/AtaLuZiK/conan-sqlite3pp/branch/release/1.0.8)|

## Reuse the packages

### Basic setup

```
conan install sqlite3pp/1.0.8@zimmerk/stable
```

### Project setup

```
[requires]
sqlite3pp/1.0.8@zimmerk/stable

[options]
# Take a look for all avaliable options in conanfile.py

[generators]
cmake
```

Complete the installitation of requirements for your project running:

```
conan install .
```

Project setup installs the library (and all his dependencies) and generates the files conanbuildinfo.txt and conanbuildinfo.cmake with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io
