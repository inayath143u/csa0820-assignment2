# Function to calculate the new character based on circular distance
def shift_character(char, shift):
    # Calculate the new character position in the alphabet
    new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
    return new_char

# Function to modify the string based on the given conditions
def modify_string(S):
    # Count the frequency of each character in the string
    frequency = {}
    for char in S:
        frequency[char] = frequency.get(char, 0) + 1

    # Create a new string with modified characters
    modified_string = ''
    for char in S:
        shift = frequency[char]
        modified_string += shift_character(char, shift)

    return modified_string

# Sample input
S = "ghee"
# Get the modified string
result = modify_string(S)

# Output the result
print(result)
