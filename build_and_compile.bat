@echo off

REM Check if the build folder exists, create it if it doesn't, and delete its contents if it does
if not exist build (
    mkdir build
) else (
    rmdir /s /q build
    mkdir build
)

REM Move into the build folder
cd build

REM Execute conan install command
conan install .. -s build_type=Debug --build missing -pr ..\windows-vs

REM Execute cmake command
cmake -G "Visual Studio 17 2022" ..

REM Execute Visual Studio build command
cmake --build .
