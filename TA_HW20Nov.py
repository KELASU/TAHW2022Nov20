class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def get_json_str(p):
    return {"__class__":p.__class__.__name__, "x":p.x , "y":p.y  }

p = Point(1,2)
z = get_json_str(p)
print(z)



def read_json_str(s):
    return Point(s['x'],s['y'])

t = read_json_str(z)
print(get_json_str(t))


