import string
def count_words(paragraph):
    paragraph = paragraph.lower()
    translator = str.maketrans('', '', string.punctuation)
    cleaned_paragraph = paragraph.translate(translator)
    words = cleaned_paragraph.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
user_input = input("Please enter a paragraph of text: ")
word_count_dict = count_words(user_input)
print("Word count:", word_count_dict)
