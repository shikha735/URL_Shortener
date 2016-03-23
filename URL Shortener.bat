@echo off
set /p long_url="Enter URL to shorten: "
cd build
main %long_url% > out.txt
pause
