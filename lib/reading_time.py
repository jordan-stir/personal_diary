def reading_time(text):
    words = text.split()
    word_count = len(words)
    return word_count / 200

import math

def reading_time(text):
    words = text.split()
    word_count = len(words)
    return math.ceil(word_count / 200)