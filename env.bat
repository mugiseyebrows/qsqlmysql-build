@echo off

if "%1" neq "--" goto all
if "%2" equ "python" set "PATH=C:\Python39-x64;C:\Python39-x64\Scripts;%PATH%"
if "%2" equ "vc" call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
if "%2" equ "jom" set "PATH=C:\Qt\Tools\QtCreator\bin\jom;%PATH%"
if "%2" equ "qt5" set "PATH=C:\Qt\5.14.2\msvc2017_64\bin;%PATH%"
if "%2" equ "qwt" set "PATH=C:\Qwt-6.2.0\lib;%PATH%"
if "%2" equ "7z" set "PATH=C:\Program Files\7-Zip;%PATH%"
if "%2" equ "git" set "PATH=C:\Program Files\Git\cmd;%PATH%"
goto end

:all
for %%x in (%*) do (
    call env -- %%x
)
:end

rem echo %PATH%