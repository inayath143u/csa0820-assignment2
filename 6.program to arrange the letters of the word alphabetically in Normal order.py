# Get input from the user
word = input("Enter the word: ")

# Convert the word to uppercase and sort the letters
sorted_word = sorted(word.upper())

# Convert the sorted list back to a string for normal order
normal_order = ' '.join(sorted_word)

# Reverse the sorted list for reverse order
reverse_order = ' '.join(sorted_word[::-1])

# Output the results
print(f"Alphabetical Order Normal: {normal_order}")
print(f"Alphabetical Order Reverse: {reverse_order}")
