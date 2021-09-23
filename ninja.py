from pet import Pet

class Ninja:

    AllNinjas = []

    def __init__ ( self, first_name , last_name, name , type , tricks ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = 3
        self.pet_food = 3
        self.pet = Pet(name , type , tricks)
        Ninja.AllNinjas.append(self)

    def walk (self): # walks the ninja's pet invoking the pet play() method
        print (f'Walking {self.pet.name}')
        Pet.play
        return self

    def feed (self, food): # feeds the ninja's pet invoking the pet eat() method
        if food == 'treats':
            if self.treats > 0:
                print (f'Feeding {food} to {self.pet.name}!')
                self.treats -= 1
                self.pet.eat()
            else:
                print (f"Oh, you do not have enough treats")
        elif food != 'treats':
            if self.pet_food > 0:
                print (f'Feeding {food} to {self.pet.name}!')
                self.pet_food -= 1
                self.pet.eat()
            else:
                print (f"Oh, you do not have enough food")
        return self

    def bathe (self): # cleans the ninja's pet invoking the pet noise() method
        print(f'Bathing {self.pet.name}')
        self.pet.noise()
        return self

    def NinjaDetails (self):
        print (f'Ninja Name: {self.first_name} {self.last_name} | Pet Name: {self.pet.name} | Food: {self.pet_food} | Treats: {self.treats}')
        return self

    @classmethod
    def AllNinjasInfo (cls):
        for instance in Ninja.AllNinjas:
            instance.NinjaDetails()

# if __name__ == "__main__":

#     NinjaPerl = Ninja('Johan', 'R.', 'Perl', 'dog', 'Stands Up')
#     NinjaLupe = Ninja('Xavier', 'R.', 'Lupe', 'cat', 'Plays Hide and Seek')

#     NinjaPerl.NinjaDetails().walk().feed('treats').feed('Banana').feed('Meat').feed('Bones').feed('Apples').bathe().NinjaDetails()
#     NinjaLupe.NinjaDetails().bathe().walk().feed('treats').feed('treats').feed('treats').feed('treats').feed('fish').NinjaDetails()
#     Pet.allpets()