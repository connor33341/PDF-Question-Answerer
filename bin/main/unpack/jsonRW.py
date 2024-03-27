# Connor W 1/12/19
"""
    A common JsonReader that has been put in use for many projects
"""
import json
class JsonReader:
    def __init__(self,File):
        self.File = File
    def Read(self):
        try:
            with open(self.File,'r') as File:
                return json.load(File)
        except Exception as Error:
            print("[ERROR]: An error has occoured while reading json file: ",Error)
    def Write(self,NewJson):
        try:
            with open(self.File,'w') as File:
                return json.dump(NewJson,File)
        except Exception as Error:
            print("[ERROR]: An error has occoured while writing json file: ",Error)