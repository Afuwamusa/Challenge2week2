# a function that takes two lists and returns the combined length using the module operator
def fizzbuzz(listx, listy):
  a = len(listx)
  b = len(listy)
  comlen = a + b
  if comlen % 3 == 0:
    return "fizz"
  elif comlen % 5 == 0:
    return "buzz"
  else:
    if comlen % 5 and comlen % 3 == 0:
      return "fizzbuzz"
print(fizzbuzz([1,2,3,4,5], [6,7,8,9]))
 



