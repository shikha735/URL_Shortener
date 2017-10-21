@echo off
set /p long_url="Enter URL to shorten: "
cd build
main %long_url% > out.txt
echo Shortening the URL. Please wait...
echo Saving the output in /build/out.txt 
echo Short url is:
type out.txt
pause
