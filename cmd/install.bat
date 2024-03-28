@ECHO off
pip install -r requirements.txt
cd tesseract
git clone https://github.com/microsoft/vcpkg
.\vcpkg\bootstrap-vcpkg.bat
mkdir main
pause