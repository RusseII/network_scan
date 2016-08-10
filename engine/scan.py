import subprocess
import json

class findRoomates():
    def __init__(self):
        print "created findRoomates object"

    def find_roomates(self):
        Roos="Russell is not home"
        subprocess.call("echo milk | sudo -S arp-scan --localnet  > allout.txt 2>&1", shell=True)
        if '64:bc:0c:65:43:22' in open('allout.txt').read():
            Roos="Russell is home"
        AJ="AJ is not Home"
        Orion="Orion is not home"

        roomates = [
        {"room":Roos,},
        {"room":AJ,},
        {"room":Orion,}
        ]
        roomates=json.dumps(roomates)
        print roomates
        return roomates
