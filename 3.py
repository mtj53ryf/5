class MethodTest:

	def inner_test(self):
		print('in class')

def outer_test():
	print('out of class')

mt=MethodTest()
mt.outer_test=outer_test
mt.inner_test()
mt.outer_test()