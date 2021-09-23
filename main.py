from ninja import Ninja
from pet import Pet

NinjaPerl = Ninja('Johan', 'M.', 'Perl', 'dog', 'Stands Up')
NinjaLupe = Ninja('Xavier', 'V.', 'Lupe', 'cat', 'Plays Hide and Seek')

NinjaPerl.NinjaDetails().walk().feed('treats').feed('Banana').feed('Meat').feed('Bones').feed('Apples').bathe().NinjaDetails()
NinjaLupe.NinjaDetails().bathe().walk().feed('treats').feed('treats').feed('treats').feed('treats').feed('fish').NinjaDetails()
print(f'*** This is the list of all pets: ***')
Pet.allpets()


