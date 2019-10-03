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
        self.PICKUP=(
            'grab','pick up', 'aquire', 'get', 'obtain'
        )
        self.DROP=(
            'drop','abandon','dump','lower','release'
        )
        self.MOVE=(
            'move','advance', 'climb','go','migrate','walk','travel','leave'
        )
        self.DIR_CONVERTER={
            'north': 'n',
            'south': 's',
            'west' : 'w',
            'east' : 'e',
            'e':'e',
            'w':'w',
            'n':'n',
            's':'s'
        }

    def move(self, direction):
        if ['n','s','e','w','west','north','south','east' in direction]:
            direction=self.DIR_CONVERTER[direction[-1]]
        else:
            print("Direction could not be read")
            return

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
    
    def give(self, *items):
        if len(items)>0:
            for item in items:
                self.inv.append(item)

    def act(self, str):
        action = str.lower().split(' ')
        if any(item in self.PICKUP for item in action):
            self.pickup(action)
        elif any(item in self.MOVE for item in action) or str in self.DIR_CONVERTER:
            self.move(action)
        else:
            print("Could not Interpret")

    def pickup(self, action):
        for item in self.currentRoom.inv:
            if any(item.key in s for s in action):
                self.inv.append(item)
                self.currentRoom.inv.remove(item)
                print(f"Picked up {item.name}")
                return

        print(f"Item not found")
    
    def drop(self, action):
        for item in self.inv:
            if item.key in action:
                self.currentRoom.inv.append(item)
                self.inv.remove(item)
                print(f"Dropped {item.name}")
                return
        print(f"Item not found")