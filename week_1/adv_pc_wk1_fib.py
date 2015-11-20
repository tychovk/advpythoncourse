'''
class FibSeq:
	def __init__(self):
		self.term = term

	def input(self):
		user_input = input("Which term of the Fibonacci sequence would you like",
		"to see?")
		if not isinstance(user_input, int) and user_input < 1:
			print ("Please choose a number between 1 and any other positive ",
			"integer!")
		else:
			print (fib(self))
			
	def recursive(self, question = "Would you love another spin? y/n"):
		user_input = input(question)
		if user_input[0].lower() == 'y':
			FibSeq.input()
			
		elif user_input[0].lower() == 'n':
			return ("Goodbye!")
			
		else:
			FibSeq.recursive(self, "Please answer with yes or no. Would you \
			love another spin?")
	
	def fib(self):
		fiblist = []
		fiblist[0] = 0
		fiblist[1] = 1
		for i in range(2, term):
			fiblist[i] = fiblist[i-1] + fiblist[i-2]
		
	

FibSeq()
'''
'''
class Fib:
	def __init__(self, max):
		self.max = max
		
	def __iter__(self):
		self.a = 0
		self.b = 1
		return self
		
	def __next__(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib

		
for n in Fib(1000):
	print (n, end=' ')
'''
	
	
class Fib:
    def __init__(self, term = 0):
        term = input("Which term of the Fibonacci sequence would you " +
             "like to see?")	
        if not term.isdigit() or term < 1:
            print ("Please choose a number between 1 and any other positive " +
                    " integer!")
            Fib(self)
        else:
            self.term = int(term)
			
    def nth_term(self, term = 0):
        print (term)
        print (self.term)
        self.a = 0
        self.b = 1
        if self.term == 1:
            return 0
        for n in range(self.term-1):
            self.a , self.b = self.b, self.a + self.b
        return self.a

    def recursive(self, question = "Would you love another spin? y/n"):
        user_input = input(question)
        if user_input[0].lower() == 'y':
            Fib.input()
			
        elif user_input[0].lower() == 'n':
            return ("Goodbye!")
			
        else:
            Fib2.recursive(self, "Please answer with yes or no. Would you \
            love another spin?")

			
hur = Fib() # creates a new instance of the Fib class

print (hur.nth_term())