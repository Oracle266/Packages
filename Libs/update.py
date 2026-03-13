import os
import json
def main():
    current_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(current_path)
    json_path = os.path.join(dir_path, "descriptor.json")
    if not (os.path.exists(json_path) and os.path.isfile(json_path)):
        with open():
        


if __name__ == "__main__":
    
