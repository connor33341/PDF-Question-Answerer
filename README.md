# PDF Question Answerer
### Notice: No longer supports MacOSx, Linux/Unix and Java
### Version: this is not the most up to date version, newer versions can be found on my discord
If someone has the time and paitence to debug and reverse engineer my installers fork and add support

---

Simple and effective way to answer questions via a PDF

## Installing
Simple and easy to install on ~~MacOSx, Linux/Unix~~ and Windows

### Windows
Least Difficult
**Requires Git and Bash**
1. `git clone connor33341/PDF-Question-Answerer`
2. `cd connor33341/PDF-Question-Answerer`
3. `installer.exe`

**If any errors occour run the following**
1. `cd cmd`
2. `install.bat`
3. `start.bat`
   
**Still errors?**
1. `bash routine.sh`
Or
1. `pip install -r requirements.txt`

**Custom Builds:**
```
git clone connor33341/PDF-Question-Answering
cd connor33341/PDF-Question-Answering
pip install -r requirements.txt
cd tesseract
git clone https://github.com/microsoft/vcpkg
.\vcpkg\bootstrap-vcpkg.bat
mkdir main
cd main
vcpkg install tesseract:x64-windows-static
```

### Linux/Unix and MacOSx
Install
1. `cd cmd`
2. `bash routine.sh`
Or
1. `pip install -r requirements.txt`

- [PDF Question Answerer](#pdf-question-answerer)
    - [Notice: No longer supports MacOSx, Linux/Unix and Java](#notice-no-longer-supports-macosx-linuxunix-and-java)
  - [Installing](#installing)
    - [Windows](#windows)
    - [Linux/Unix and MacOSx](#linuxunix-and-macosx)

 
