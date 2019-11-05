#1. import random
#ls = random.sample(range(100),30)
#print(ls)

class Test():

	def __init__(self,name,id_):
		self.name = name
		self.id_ = id_

	def show_name(name,id_):
		test = Test(name,id_)
		return test

ls = Test("Name", 99)
Test.show_name
print(ls)


# 5. weekdays = ['sun','mon','tye','sun','mon']
#ls = set(weekdays)
#print(ls)
