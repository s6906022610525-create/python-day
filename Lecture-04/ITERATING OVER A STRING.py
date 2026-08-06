input_string = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        modifiled_string += "*"
    else:
        modified_string += upper_char
    print("Modifiled string:", modifiled_string)
    