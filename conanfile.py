from conans import ConanFile, CMake, tools


class UdsServerConan(ConanFile):
    name = "demo_app"
    version = "1.0.0"
    license = ""
    url = "https://github.com/ibosnic00/demo_cmake_conan.git"
    description = ""
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    target_name = "demo_app"

    def source(self):
        self.run(
            "git clone https://github.com/ibosnic00/demo_cmake_conan.git")
        self.run("cd demo_cmake_conan")

    def requirements(self):
        self.requires("protobuf/3.17.1")
        self.requires("zlib/1.2.13")

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        if self.settings.build_type == "Debug":
            self.copy("*.pdb", "bin", "bin")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="demo_cmake_conan")
        cmake.build(target=self.target_name)

    def package(self):
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.pdb", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs.append(self.target_name)
