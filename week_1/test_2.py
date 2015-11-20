try:
	import humansize
except ImportError:
	chardet = None

"""To make sure there is at least a module imported, even if it's not the best one"""
try:
	from lxml import etree
except ImportError:
	import xml.etree.ElementTree as etree
	
a_list = ['a','b','mpilgrim','z','z','example']


print ("""{}
{}
{}
"""
.format(a_list[1:3] , 
a_list[1:-1] , 
a_list[0:3]))

def diff(a,b):
	b = set(b)
	return [aa for aa in a if aa not in b]

list_a = [1,4,6,8,3,7,4,9,0,44,66,88]
list_b = [1,2,3,4,5,6,44,5]
print (diff(list_a,list_b))
