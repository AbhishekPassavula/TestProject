class Graph:
    def __init__(self):
        print("Constructor class")
    def getPaths(self,start,end,path=[]):
        print("print paths")
        

if __name__=='__main__':
    g=Graph()
    start="Mumbai"
    end="Hyderbad"
    g.getPaths(start,end)
