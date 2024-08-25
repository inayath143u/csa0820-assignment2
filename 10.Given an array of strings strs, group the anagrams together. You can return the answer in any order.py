from collections import defaultdict

def group_anagrams(strs):
    # Initialize a default dictionary to hold lists of anagrams
    anagrams = defaultdict(list)
    
    # Iterate through each string in the list
    for s in strs:
        # Sort the string and use the sorted tuple as the key
        key = tuple(sorted(s))
        # Append the original string to the list of anagrams for that key
        anagrams[key].append(s)
    
    # Convert the dictionary values to a list of lists
    return list(anagrams.values())

# Sample input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Get the grouped anagrams
result = group_anagrams(strs)

# Output the result
print(result)
