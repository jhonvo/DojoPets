from ninja import Ninja #Calling the required classes
from pet import Pet #Calling the required classes

NinjaPerl = Ninja('Johan', 'M.', 'Perl', 'dog', 'Stands Up') #Creating both Ninjas and Pets on the same line
NinjaLupe = Ninja('Xavier', 'V.', 'Lupe', 'cat', 'Plays Hide and Seek') #Creating both Ninjas and Pets on the same line

NinjaPerl.NinjaDetails().walk().feed('treats').feed('Banana').feed('Meat').feed('Bones').feed('Apples').bathe().NinjaDetails()
NinjaLupe.NinjaDetails().bathe().walk().feed('treats').feed('treats').feed('treats').feed('treats').feed('fish').NinjaDetails()
print(f'*** This is the list of all pets: ***')
Pet.allpets() #Calling a Class Method on the Pet class


