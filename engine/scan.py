import subprocess
import json


class findRoomates():
    def __init__(self):
        print "created a findRoomates object"

    def find_roomates(self):
        subprocess.call("echo milk | sudo arp-scan --localnet  > allout.txt", shell=True)
        roomates = {}
        roomates['roos'] = False

        if '64:bc:0c:65:43:22' in open('allout.txt').read():
            roomates['roos'] = True
 
        roomates = json.dumps(roomates)
        print roomates
        return roomates
