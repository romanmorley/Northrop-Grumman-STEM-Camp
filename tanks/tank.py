#a template for creating Tank objects

class Tank(object):
    def __init__(self,name):
        self.name = name
        self.armour = 20
        self.ammo = 10
        self.alive = True
    #This is how we represent our tank as a string
    def __str__(self):
        if self.alive:
            return '%s (%i ammo,%i armour)' % (self.name,self.ammo,self.armour)
        else:
            return '%s (DEAD)' %self.name
    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, 'fires', enemy.name)
            enemy.hit
        else:
            print(self.name, 'has no ammo!')
    #We take a hit, if it breaks our shields, the tank explodes
    def hit(self):
        self.armour -= 5
        print(self.name, 'is hit!')
        if(self.armour <= 0):
            self.explode()
    def explode(self):
        print(self.name, 'explodes!')
        self.alive = False
