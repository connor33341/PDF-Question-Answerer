import os
import subprocess
from jsonRW import JsonReader

class Main:
    def __init__(self,Config):
        self.Config = Config
        self.Reader = JsonReader(self.Config)
        self.ReaderData = self.Reader.Read()
    def ValidateOS(self):
        self.ValidOS = False
        if self.OS == "nt":
            print("[INFO]: Building for Windows")
            self.ValidOS = True
    def Run(self):
        self.OS = None
        self.OS = os.name
        self.ValidOS = False
        #self.ValidateOS()
        while self.ValidOS == False:
            print("[WARN]: Failed to identify OS")
            print("[MSG]: Please type posix for Linux/Unix based system or nt for Windows based system, java for java systems")
            self.OS = str(input()).lower()
            self.ValidateOS()
        print("[INFO]: OS Validated")
        if self.OS == "nt":
            try:
                pass
            except (Exception) as Error:
                print(f"[ERROR]: {Error}")
        elif self.OS == "posix":
            try:
                pass
            except (Exception) as Error:
                print(f"[ERROR]: {Error}")
        elif self.OS == "java":
            print("[ERROR]: BUILD NOT SUPPORTED IN JAVA")
            raise RuntimeError("[BUILD-RTE]: Error Raised")

if __name__ == "__main__":
    Directory = os.getcwd()
    print(f"[INFO]: Using CWD: {Directory}")
    MainClass = Main(f"{Directory}\\bin\main\config.json")
    try:
        print("[INFO]: MainClass Begin")
        MainClass.Run()
    except (Exception) as Error:
        print(f"[ERROR]: {Error}")
        os.system("pause")