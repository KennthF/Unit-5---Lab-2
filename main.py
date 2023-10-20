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
                
    file.write(f"This is all the consonant in the sample.ini;\n\n{count_dict}") #Write on that file
    file.close() #Close the count file
    

new_file = open(f"count.txt", "w") #Creates the count file
with open("./sample.ini", "r") as sample_file: #Open the sample file
        data = sample_file.read()

count_consonant(data,new_file) #Writes in the count file

with open("./count.txt", "r") as count_file: #Open and Read the count file
        new_file = count_file.read()

print(new_file)

count_file.close()
sample_file.close()