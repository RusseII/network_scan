import subprocess
import json

class findRoomates():
    def __init__(self):
        print "created findRoomates object"

    def find_roomates(self):
        Roos="Russell is not home"
        Grace="Grace is not in my appartment"
        subprocess.call("echo milk | sudo -S arp-scan --localnet  > allout.txt 2>&1", shell=True)
        if '64:bc:0c:65:43:22' in open('allout.txt').read():
            Roos="Russell is home"


            if '12:b3:b7:d2:e2:3d' in open('allout.txt').read():
                Grace="Grace is at my appartment"
        AJ="AJ is not Home"
        Orion="Orion is not home"

        roomates = [
        {"room":Roos,},
        {"room":AJ,},
        {"room":Orion,},
        {"room":Grace,}
        ]
        roomates=json.dumps(roomates)
        print roomates
        return roomates
