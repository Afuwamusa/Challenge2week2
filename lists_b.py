#creating a function that returns a string of vowels and the number of letters that appear more than once in a sentence.
def vowels(string_listx):
    #it's creating a variable that holds the sentence entered
    string_list = string_listx.lower().split(' ')
    #creating an empty string  to hold characters entered by the user
    y = ''

    for word in string_list:
    #adding characters in the empty string created above.
        y += word
    #creating a list of vowels
    vowels = ['a','e','i','o','u']
    # using a list comprehation to retun vowels in string y
    vowels_in_string = [vowel for vowel in vowels if vowel in y]
    #creating an empty sring to hold the vowels in the sentence
    vowels_string = ""
    #looking through the vowels  in the list comprehation
    for vowel in vowels_in_string:
    #adding the vowel in the empty string
        vowels_string =vowels_string + vowel
    #creating an empty list to hold the duplicates
    t = []
    #adding all duplicates in the empty list that appear more than once and should not be repeated
    x = [t.append(letter) for letter in y if y.count(letter) > 1 and letter not in t]
    #returning the vowels and the number of duplicates in the sentence
    results = (vowels_string , len(t))
    return results
print(vowels("type a sentence: ")) 
    
