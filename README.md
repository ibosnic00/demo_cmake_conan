## Prerequisites:

- working **conan** ```Conan version 1.57.0 or newer```
- working **cmake** ```cmake version 3.23.0-rc or newer```
- Microsoft Visual Studio 2022 compiler



### Steps to reproduce issue:

- open conanfile.py and on line 22 make sure the version of protobuf is 3.17.1 or newer ```self.requires("protobuf/3.17.1")```

- start build_and_compile.bat script ```.\build_and_compile.bat```

### Steps to reproduce issue manually:

- open conanfile.py and on line 22 make sure the version of protobuf is 3.17.1 or newer ```self.requires("protobuf/3.17.1")```

- position yourself to build folder ```cd build``` (make sure its empty)
- execute conan install command with profile from repository ```conan install .. -s build_type=Debug --build missing -pr ..\windows-vs ```
- execute cmake generator selection ```cmake -G "Visual Studio 17 2022"  ..```
- start build with ```cmake --build .```

### Steps to have working version:

- open conanfile.py and on line 22 make sure the version of protobuf is 3.16.0 or older ```self.requires("protobuf/3.16.0")```