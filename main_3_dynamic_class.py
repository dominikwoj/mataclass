def __init__(self, name: str, surname: str, year_of_birth: int):
    self.name = name
    self.surname = surname
    self.year_of_birth = year_of_birth


attrs = {
    '__init__': __init__
}

Person = type('Person', (), attrs)
print(type(Person)) # show: <class 'type'>
print(dir(Person))

person = Person('Dominik', 'Wojnowski', 1981)
print(dir(person))