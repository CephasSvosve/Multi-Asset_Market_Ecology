class watch:
    def __init__(self,dt):
        self.t  = 0
        self.dt = dt
    def time(self):
        return self.t
    def start(self):
        self.t = 0
        return self.t
    def reset(self):
        self.t = 0
        return self.t
    def tick(self):
        self.t +=self.dt
        return self.t


