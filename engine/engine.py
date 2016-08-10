from scan import findRoomates

class Engine():
    def __init__(self):
        print "created engine object"

    def execute(self):
        roomies = findRoomates()
        return roomies.find_roomates()
