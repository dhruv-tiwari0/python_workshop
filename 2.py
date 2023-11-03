'''name="dhruv"
print(len(name))

age=24
if age>=18:
    print("you are adult")
else:
    print("you are minor")

score=85
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
else:
    print("F")

raining=True
cold=True
if raining:
   print("bring an umbrella")
if cold:
    print("bring a jacket") 

number=0
if number>0:
 print("positive")
elif number<0:
 print("negative") 
else:
 print("0")

#unordered collection of unique elements in python are sets.      
set={1,2,3} 
set.add(6)
print(type(set))
set.remove(3)
set.discard(3)
set1={7,8,9}
print(set.union(set1))
print(set.intersection(set1))
print(set.difference(set1))'''

'''def intersection(set,set1):
    find=set.intersection(set1)
    return find
set={"a","b","c","d"}
set1={"e","b","d"}
b=(intersection(set,set1))
print(b)'''

s=[1,2,3]
print(set(s))




