# from https://discourse.processing.org/t/trying-to-understand-the-substrate-algorithm/3031/4
# by j.tarbell ported to Python by solub

num, n_agents = 0, 100

def setup():
    global collection, grid
    size(1200, 900, P2D)
    background(255)
    smooth(8)
    
    grid = [10001 if random(1) > .00003 else int(random(360)) for e in range(width*height)]
    collection = [Agent() for e in range(n_agents)]
    for e in range(3): addAgent()

def draw():
    for a in range(num):
        collection[a].move()
        collection[a].findEdge()
        
def addAgent():
    global num
    if num < n_agents:
        collection[num] = Agent()
        num += 1
    
class Agent(object):
    def __init__(self):
        self.location = PVector(int(random(width)), int(random(height)))
        self.angle = 0.0
        self.findStart()
        
    def findStart(self):
        found  = False
        while not found:
            px, py = int(random(width)), int(random(height))
            if grid[px + py * width] < 10000: found = True
            
        if found:
            a = grid[px + py * width]
            self.angle = a + 90 if random(1) > .5 else a - 90
            self.location = PVector(px, py)
       
    def move(self):
        self.location += PVector(cos(radians(self.angle)), sin(radians(self.angle)))
        point(self.location.x, self.location.y)
        
    def findEdge(self):
        x, y = int(self.location.x), int(self.location.y)
        index = x + y * width

        if x >= 0 and x < width and y >= 0 and y < height:
            
            if grid[index] > 10000 or abs(grid[index]-self.angle) < 10: 
                grid[index] = int(self.angle)  

            else: self.findStart(); addAgent()
            
        else: self.findStart(); addAgent()
