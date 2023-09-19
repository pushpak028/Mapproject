import json

def load1(filepath):
    with open(filepath,'r') as file1:
        data:dict = json.load(file1)
    
    return data


