# import pyglet
import random
import flask
import block
from loadSource import *
import ujson as json
from io import BytesIO
app = flask.Flask("builders mine server")
def save(world):
    ##  @brief save the player position and world into the file
    worlds = {}
    for b in list(world.items())[0:2]:
        print(b)
    # buffered = BytesIO()
    for block in ALLBLOCKS:
        worlds[block.name] = []
    for i in world.keys():
        try:
            worlds[world[i]].append(i)
        except Exception as e:
            pass
            # print("error: {}".format(e))
         
    data = {"position":[10, 10, 10],"world":worlds}
    
    buffered = json.dumps(data)
    return json.loads(buffered)
class data:
    def __init__(self):
        self.world = {}
        self.blocks = {}
        self.untilbedrock = 40
        for block in ALLBLOCKS:
            self.blocks[block.name] = block
        self.setupWorld()
        self.hill()
        self.tree()
    def hill(self, n=80, count=20):
        o = 70
        for _ in range(count):
            a = random.randint(-o, o)  
            b = random.randint(-o, o)  
            c = -1  
            h = random.randint(1, 150)  
            s = random.randint(4, 10)  
            d = 1  
            t = random.choice([GRASS, STONE, DIRT])
            for y in range(c, c + h):
                for x in range(a - s, a + s + 1):
                    for z in range(b - s, b + s + 1):
                        if (x - a) ** 2 + (z - b) ** 2 > (s + 1) ** 2:
                            continue
                        if (x - 0) ** 2 + (z - 0) ** 2 < 5 ** 2:
                            continue
                        self.add_block((x, y, z), t.name, immediate=False)
                s -= d  
    def setupWorld(self):
        """ Initialize the world by placing all the blocks.
        """
        n = 100  # 1/2 width and height of world
        s = 1  # step size
        y = 0  # initial y height
        for x in range(-n, n + 1, s):
            for z in range(-n, n + 1, s):
                # create a layer MARBLE.coordinates an GRASS.coordinates everywhere.
                self.add_block((x, y - 2, z), GRASS.name, immediate=False)
                for i in range(3, self.untilbedrock):
                    self.add_block((x, y - i, z), STONE.name, immediate=False)
                self.add_block((x, y - self.untilbedrock, z), MARBLE.name, immediate=False)
                if x in (-n, n) or z in (-n, n):
                    # create outer walls.
                    for dy in range(-self.untilbedrock, 3):
                        self.add_block((x, y + dy, z), MARBLE.name, immediate=False)

    def add_block(self, position, block, immediate=True):
        if block not in self.blocks:
            raise ValueError("The block cannot be recognized in this world.")
        if position in self.world:
            self.remove_block(Begin=True, position=position, immediate=immediate)
        self.world[position] = block
    def remove_block(self, position, immediate=True, Begin=False):
        if position not in self.world:
            raise ValueError("There is not block at the given position")
        Begin = not Begin
        if Begin:
            block = self.world[position]
        del self.world[position]
        if Begin:
            return block
    def _leave(self, a, h, b):
        self.add_block((a, h, b), LEAVES.name, immediate=False)
    def tree(self, n=80, count=25):
        l = self._leave
        o = n - 10
        for i in range(count):
            height = random.randint(5, 7)
            a = random.randint(-o, o)  
            b = random.randint(-o, o)
            for _ in range(-1, height):
                self.add_block((a, _, b), WOOD.name, immediate=False)
                h = height - 1
                #leaves
                l(a, h, b+1)
                l(a, h, b-1)
                l(a+1, h, b+1)
                l(a+1, h, b-1)
                l(a-1, h, b+1)
                l(a-1, h, b-1)
                l(a-1, h, b)
                l(a+1, h, b)
                #top of tree
                self.add_block((a, h+1, b), LEAVES.name, immediate=False)
@app.route("/")
def jsonobj():
    d = data()
    d.hill()
    print(len(str(d.world)))
    return save(d.world)
    # return str(d.world)
app.run(debug=True)
