'''
for x in range(100,1100,100):
    print(x)

 '''
 '''   
for x in xrange(100,1100,100):
    print(x)
'''
both will give same output
range():

The range is an inbuilt function that generates the list. It creates a static list before running the iteration.

xrange():

Unlike range, xrange returns xrange sequence object.
Using xrange is safe when dealing with larger numbers.