from person_start import Person 
bob = Person('Bob Smith', 42) 
sue = Person('Sue Jones', 45, 40000)
people = [bob, sue]                          # a "database" list 
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people] 
print(x)
x=[rec.name for rec in people if rec.age >= 45]     # SQL-ish query
print(x)
x=[(rec.age ** 2 if rec.age >= 45 else rec.age) for rec in people]
print(x) 