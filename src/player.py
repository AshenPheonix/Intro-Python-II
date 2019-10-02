# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, room=None):
        self.currentRoom=room
        self.inv=[]
        self.directions={
            "n":self.currentRoom.n_to,
            "s":self.currentRoom.s_to,
            "e":self.currentRoom.e_to,
            "w":self.currentRoom.w_to
        }

    def move(self, direction):
        if self.directions.get(direction,'Improper Action') != None:
            self.currentRoom=self.directions[direction]
            self.directions={
                "n":self.currentRoom.n_to,
                "s":self.currentRoom.s_to,
                "e":self.currentRoom.e_to,
                "w":self.currentRoom.w_to
            }
            print(f"Moved to the {self.currentRoom.name}")
        else:
            print("No room there")