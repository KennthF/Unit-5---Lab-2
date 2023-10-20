def count_consonant(info):
    # Count the consonant of a file
    vowels = ["a","e","i","o","u"]
    count_dict = {}
    for char in info:
        if char not in vowels:
            value = count_dict.get(char) #Put the element to the key (The left side)

            if value is None:  #Check if it is empty (Its right side)
                count_dict[char] = 1 #Add zero to it

            else:
                count_dict[char] += 1 #if not empty plus 1
    return count_dict


#Open the sample file, and create the count file
with open("./sample.ini", "r") as sample_file:
    data = sample_file.read()

dict_content = count_consonant(data) #Put the files inside the functions

#Write the counted consonant and/or create the count file
with open("./counts.txt", "w") as count_file: 
    count_file.write(f"This is all the consonant in the sample.ini;\n\n{dict_content}\n") 
    
#Read the counted file    
with open("./counts.txt", "r") as count_read:
    file_count = count_read.read()

print(file_count)
