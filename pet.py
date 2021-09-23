class Pet:

    pet_list = []

    def __init__ ( self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        Pet.pet_list.append(self)

    def sleep (self): # increases the pets energy by 25
        self.energy += 25
        return self

    def eat (self): # increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        return self

    def play (self): # increases the pet's health by 5
        self.health += 10
        return self

    def noise (self): # prints out the pet's sound
        if self.type == 'cat':
            print('Meow! Meow! Meow!')
        elif self.type == 'dog':
            print('Guau! Guau! Guau!')
        else:
            print('Nooo! Nooo!')
        return self

    def pet_info (self):
        print (f'Pet Name: {self.name} | A {self.type} | Talent: {self.tricks} | Energy: {self.energy} | Health: {self.health}')
        return self

    @classmethod
    def allpets (cls):
        for instance in cls.pet_list:
            # print(instance)
            instance.pet_info()

# if __name__ == "__main__":
#     Perla = Pet('Perla', 'dog', 'Sings')
#     Lupita = Pet('Lupita', 'dog', 'Looks')
#     Pedro = Pet('Pedro', 'cat', 'touch')

#     Pedro.noise()
#     Lupita.eat()
#     Perla.play()

#     Pet.allpets()