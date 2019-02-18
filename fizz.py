# a function that takes two lists and returns the combined length using the module operator
def fizzbuzz(listx, listy):
#creating varriables and giving length to the lists in the function
  a = len(listx)
  b = len(listy)
# combining the two lists
  comlen = a + b
#creating a conditional statement to return fizz if divisible by 3
  if comlen % 3 == 0:
    return "fizz"
#creating a conditional statement to return buzz if divisible by 5
  elif comlen % 5 == 0:
    return "buzz"
#creating a conditional statement to return fizzbuzz if divisible by 5 and 3 
  elif comlen % 5 and comlen % 3 == 0:
      return "fizzbuzz"
#returning the combined length
  else: 
    return comlen
  
  
print(fizzbuzz([1,2,3,4,5], [6,7,8,9]))
 



