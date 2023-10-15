string = input("Enter a string: ")


if len(string) < 2:
    print("Error: String is too short.")
else:
    
    char_counts = {}

    
    for char in string:
        
        if char in char_counts:
            char_counts[char] += 1
        
        else:
            char_counts[char] = 1

    
    sorted_items = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    
    print("The second-most occurring character is:", sorted_items[1][0])