import os
import shutil

from conans import CMake, ConanFile, tools


class Sqlite3ppConan(ConanFile):
    name = "sqlite3pp"
    version = "1.0.8"
    license = "Public Domain"
    url = "https://github.com/iwongu/sqlite3pp"
    description = "C++ wrapper of SQLite3 API."
    settings = "os", "compiler", "build_type", "arch"
    requires = "sqlite3/3.21.0@bincrafters/stable"
    exports = ["CMakeLists.txt"]
    exports_sources = ["FindSQLite3PP.cmake"]
    generators = "cmake"

    def source(self):
        self.run("git clone %s" % self.url)
        self.run("cd %s && git checkout v%s" % (self.name, self.version))

    def build(self):
        shutil.move("CMakeLists.txt", "CMakeLists.txt")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="sqlite3pp/src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["sqlite3pp"]
