import pydoc, os
def sep(s, n):
	print s * n
choice = " "
choices = ["file", "print"]
print
print "-*-"
print """Welcome to the Python Search Program. Type in a keyword or term and it pulls up the 
document for your input."""
print "-*-"
print
sep("-", 50)
ask = raw_input("What Would You Like To Search? ")
sep("-", 50)
print
try:
	doc = pydoc.plain(pydoc.render_doc(eval(ask)))
	sep("=", 50)
	print "Type 'File' to write Your Document To a File Called 'pydoc.txt'. "
	print "Type 'Print' to print Your Document."
	while choice not in choices:
		choice = raw_input("").lower()
	sep("=", 50)
	print
	if choice == choices[0]:
		with open('pydoc.txt', 'w') as myfile:
			myfile.write(doc + "\n")
			print """File Written.
			"""
	elif choice == choices[1]:
		sep("#", 50)
		print doc
		sep("#", 50)
		print
except (NameError, AttributeError, SyntaxError):
	print "Please Clarify Your Input."