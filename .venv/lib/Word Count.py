def word_count(sentence, word):
    count = 0
    for i in sentence:
        if i == word:
            count += 1
    return count

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
lower_sentence = sentence.lower()
countmain = word_count(lower_sentence, word)
print("Number of words in the sentence:", countmain)