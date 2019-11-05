class Person:
	pass

class Employee(Person):
	def __init__(self, obj_name, obj_id):
		self.obj_name = obj_name
		self.obj_id = obj_id
	def properties(self):
		print(self.obj_name)
		print(self.obj_id)
print('The question number 2.\n')
employee1 = Employee("This is name: Ann", "This is id: 11")
#employee2 = Employee("David", "34")
employee1.properties()
#employee2.properties()
print("\n")

