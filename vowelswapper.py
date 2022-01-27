def vowel_swapper(string):

    string=string.replace('a',"4")
    string=string.replace('A',"4")

    string=string.replace('e',"3")
    string=string.replace('E',"3")

    string=string.replace('i',"!")
    string=string.replace('I',"!")

    string=string.replace('o',"ooo")
    string=string.replace('O',"000")
    
    string=string.replace('u',"|_|")
    string=string.replace('U',"|_|")

    return string

print(vowel_swapper("aA eE iI oO uU"))
print(vowel_swapper("Hello World"))
print(vowel_swapper("Everything's Available")) 
print(vowel_swapper("I've got a lovely bunch of coconuts")) 
print(vowel_swapper("I like Peter Sagan, and Wout Van Aert and Matty Van Der Poel are similar talents")) 
print(vowel_swapper("Alejandro Valverdi loves a good blood bag, so much he named it after his German Shepherd. Such a Piti")) 
print(vowel_swapper("Superman Lopez couldnt pull the skin off a rice pudding"))