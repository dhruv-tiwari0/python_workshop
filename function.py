#local varaible
'''def function():
   x=10#x is a local scope
   print(x)
function()'''   

'''def function():
   a=10
   b=20
   c=a+b
   print(c)
function()   
'''

#global variable
'''def function():
   print(x)
x=10#x is a global scope   
function()'''

#non-local scope
def modifyglobal():

    x=20
x=10    
modifyglobal() 
print(x)   