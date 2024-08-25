# Get input from the user
word = input("Enter the word: ")

# Convert the word to uppercase for consistency
word = word.upper()

# Dictionary to store the frequency of each letter
letter_count = {}

# Iterate through the word to count each letter
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

# List to store the repeated letters
repeated_letters = []

# Find letters that appear more than once
for letter, count in letter_count.items():
    if count > 1:
        repeated_letters.append(letter)

# Output the results
print(f"Number of repeated letters = {len(repeated_letters)}")
if repeated_letters:
    print(f"Repeated letter(s) = {' '.join(repeated_letters)}")
else:
    print("No letters are repeated.")
