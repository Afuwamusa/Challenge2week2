#a function that takes a string and returns a tuple
string_list = input("enter a sentence: ").lower().split(' ')
y = ''

for word in string_list:
    y += word
vowels = ['a','e','i','o','u']
vowels_in_string = [vowel for vowel in vowels if vowel in y]
vowels_string = ""
for vowel in vowels_in_string:
    vowels_string =vowels_string + vowel
t = []
x = [t.append(letter) for letter in y if y.count(letter) > 1 and letter not in t]

print(x)
results = (vowels_string , len(t))
print(results) 
    
