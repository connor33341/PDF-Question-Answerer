import os
from transformers import pipeline
from jsonRW import JsonReader
import argparse
import logging
import torch
import uuid

# & C:/Users/Connor/AppData/Local/Microsoft/WindowsApps/python3.10.exe d:/GitHub/PDF-Question-Answerer/bin/main/unpack/main.py --file
class Main:
    def __init__(self,Config,Dir):
        self.Config = Config
        self.Dir = Dir
        self.ID = uuid.uuid4()
        self.LoggerDir = f"{self.Dir}\\log\\{self.ID}.log"
        self.Reader = JsonReader(self.Config)
        self.ReaderData = self.Reader.Read()
        self.AutoValid = self.ReaderData["auto-valid"]
        self.QAModel = self.ReaderData["qamodel"]
        self.Purpose = self.ReaderData["purpose"]
        self.Filename = os.path.basename(__file__)
        self.ArgParser = argparse.ArgumentParser(description=f"use {self.Filename}")
        self.ArgParser.add_argument("--setfile",type=str)
        self.ArgParser.add_argument("--file",type=str)
        self.ArgParser.add_argument("--usefile",type=bool)
        self.Args = self.ArgParser.parse_args()
        logging.basicConfig(level=logging.INFO, format='[%(asctime)s|%(levelname)s]: %(message)s')
        self.Logger = logging.getLogger(__name__)
        self.QAPipe = pipeline(
            self.Purpose,
            model=self.QAModel
        )
        """
        parser.add_argument('integers', metavar='N', type=int, nargs='+'
        """
    def Analyize(self):
        self.FileDir = self.Args.file
        print(f"[FILESYSTEM]: Attempting Dir: {self.FileDir}")
        if self.FileDir:
            ValidDir = os.path.isdir(self.FileDir)
            if ValidDir:
                print("[FILESYSTEM]: Directory Validated")
                print("[INFO]: Waiting for Question")
                self.Question = input("[INPUT]: ")
                self.Result = self.QAPipe(
                    self.FileDir,
                    self.Question
                )
            else:
                print(f"[FILESYSTEM]: Invalid Dir: {self.FileDir}")
                print("[ERROR]: The cause of this error is above")
        else:
            print(f"[ERROR]: No file set, use {self.Filename} --file <filedirhere>")
    def ValidateOS(self):
        self.ValidOS = False
        if self.OS == "nt":
            print("[INFO]: Building for Windows")
            self.ValidOS = True
        elif self.OS == "posix":
            print("[INFO]: Building for Linux/Unix")
            self.ValidOS = True
        elif self.OS == "custom":
            self.ValidOS = True
    def Run(self):
        self.OS = None
        self.OS = os.name
        self.ValidOS = False
        if self.AutoValid:
            self.ValidateOS()
        else:
            print("[WARN]: Auto-Valid is off, consider enabling to prevent OS ID errors")
        while self.ValidOS == False:
            print("[WARN]: Failed to identify OS")
            print("[MSG]: Please type posix for Linux/Unix based system or nt for Windows based system, java for java systems")
            self.OS = str(input("[INPUT]: ")).lower()
            self.ValidateOS()
        print("[INFO]: OS Validated")
        if self.OS == "nt":
            try:
                self.Analyize()
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
    MainClass = Main(f"{Directory}\\bin\main\config.json",Directory)
    try:
        print("[INFO]: MainClass Begin")
        MainClass.Run()
    except (Exception) as Error:
        print(f"[ERROR]: {Error}")
        os.system("pause")
    print("[SYSTEM]: Program Ended")
    os.system("pause")