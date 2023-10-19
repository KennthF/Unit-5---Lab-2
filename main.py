def count_consonant(info,file):
    vowels = ["a","e","i","o","u"]
    count_dict = {}
    for char in info:
        if char not in vowels:
            value = count_dict.get(char) #Put the element to the key (The left side)

            if value is None:  #Check if it is empty (Its right side)
                count_dict[char] = 1 #Add zero to it
            else:
                count_dict[char] += 1 #if not empty plus 1
    
    