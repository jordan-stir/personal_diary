from lib.reading_time import *

def test_empty_string_returns_0():
    result = reading_time("")
    assert result == 0

def test_200_words_returns_1():
    text = "word " * 200
    result = reading_time(text)
    assert result == 1

def test_400_words_returns_2():
    text = "word " * 400
    result = reading_time(text)
    assert result == 2

def test_250_words_round_up_to_2():
    text = "word " * 250
    result = reading_time(text)
    assert result == 2