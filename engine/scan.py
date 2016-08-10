import subprocess
import json


class findRoomates():
    def __init__(self):
        print "created a findRoomates object"

    def find_roomates(self):
        subprocess.call("echo milk | sudo arp-scan --localnet  > allout.txt", shell=True)
        roomates = {}

        if '64:bc:0c:65:43:22' in open('allout.txt').read():
            roomates['Roos'] = True
 
        print roomates
        return roomates
