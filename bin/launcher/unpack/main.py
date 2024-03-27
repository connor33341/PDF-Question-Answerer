import os
import subprocess
from jsonRW import JsonReader

class Launcher:
    def __init__(self,Config):
        self.Config = Config
        self.Reader = JsonReader(self.Config)
        self.ReaderData = self.Reader.Read()
        self.Message = self.ReaderData["message"]
        self.Pause = self.ReaderData["pause"]
    def ValidateOS(self):
        self.ValidOS = False
        if self.OS == "nt":
            print("[INFO]: Building for Windows")
            self.ValidOS = True
        elif self.OS == "posix":
            print("[INFO]: Building for Linux/Unix")
            self.ValidOS = True
        elif self.OS == "java":
            print("[WARN]: Java is not fully supported")
            self.ValidOS = True
    def Run(self):
        self.Routine = self.ReaderData["routine"]
        self.Method = self.ReaderData["method"]
        self.Start = self.ReaderData["start"]
        self.Install = self.ReaderData["install"]
        self.OS = None
        self.OS = os.name
        self.ValidOS = False
        self.ValidateOS()
        while self.ValidOS == False:
            print("[WARN]: Failed to identify OS")
            print("[MSG]: Please type posix for Linux/Unix based system or nt for Windows based system, java for java systems")
            self.OS = str(input()).lower()
            self.ValidateOS()
        print("[INFO]: OS Validated")
        if self.OS == "nt":
            try:
                subprocess.run([self.Start],shell=True)
                subprocess.run([self.Install],shell=True)
            except (Exception) as Error:
                print(f"[ERROR]: {Error}")
        elif self.OS == "posix":
            try:
                subprocess.run([f"{self.Method} {self.Routine}"])
            except (Exception) as Error:
                print(f"[ERROR]: {Error}")
        elif self.OS == "java":
            print("[ERROR]: BUILD NOT SUPPORTED IN JAVA")
            raise RuntimeError("[BUILD-RTE]: Error Raised")

if __name__ == "__main__":
    LauncherClass = Launcher("bin/launcher/unpack/config.json")
    try:
        print("[INFO]: LauncherClass Begin")
        print(f"[MSG]: {LauncherClass.Message}")
        if LauncherClass.Pause:
            print("[INFO]: Setup Paused")
            os.system("pause")
            print("[INFO]: Starting")
        else:
            print("[INFO]: Starting")
    except (Exception) as Error:
        print(f"[ERROR]: {Error}")
        os.system("pause")