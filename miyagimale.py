class Person:
    def __init__(self,name,isMale):
        self.name=name
        if (isMale==True):
            self.sex="Male"
        else:
            self.sex="Female"
    def  show(self):
            print("%s  is  %s" %  (self.name,self.sex))

ListOfPerson=[]
ListOfPerson.append(Person("Alice",False))
ListOfPerson.append(Person("BJ",True))
ListOfPerson.append(Person("Carol",False))

ListOfMale=[]
ListOfFemale=[]

for person in ListOfPerson:
    if (person.sex=="Male"):
        ListOfMale.append(person)
    else:
        ListOfFemale.append(person)
print("")
print("Male")
for person in ListOfMale:
        person.show()
    
print ("")
print ("Female")
for person in ListOfFemale:
            person.show()
