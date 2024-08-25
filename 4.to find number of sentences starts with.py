# Sample input
text = """The apple doesn't fall. 
All that glitters are not gold. 
A picture is worth a thousand words. 
Beggers can't be choosers. 
A bird in the hand. 
Better safe than sorry. 
An apple a day keeps doctor away. 
Blood is thicker than water."""

# Splitting the text into sentences
sentences = text.splitlines()

# Counting the total number of sentences
total_sentences = len(sentences)

# Counting the number of sentences that start with 'B'
b_sentences = sum(sentence.strip().startswith('B') for sentence in sentences)

# Output
print("Total number of lines:", total_sentences)
print("Number of Sentences that start with letter B:", b_sentences)
