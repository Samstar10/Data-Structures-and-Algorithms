import string

def word_frequency(sentence):
    translator = str.maketrans("", "", string.punctuation)
    clean_sentence = sentence.translate(translator).lower()

    word_count = {}
    words = clean_sentence.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count