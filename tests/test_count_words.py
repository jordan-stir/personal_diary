from lib.count_words import *

def test_one_word_returns_1():
    result = count_words("hello")
    assert result == 1

def test_two_words_returns_2():
    result = count_words("hello world")
    assert result == 2

def test_empty_string_returns_0():
    result = count_words("")
    assert result == 0

def test_extra_spaces_still_counts_words():
    result = count_words(" lots  of   spaces  ")
    assert result == 3