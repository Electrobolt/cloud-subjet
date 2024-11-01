from pyVim.connect import SmartConnect
import json
import ssl

def connect():
    context = ssl._create_unverified_context()
    si = SmartConnect(host="esxi_host", user="root", pwd="password", sslContext=context)
    return si.RetrieveServiceContent()
    

def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
