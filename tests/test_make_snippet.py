from lib.make_snippet import *

def test_one_word_returns_same_word():
    result = make_snippet("hello")
    assert result == "hello"

def test_five_words_returns_same_five_words():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_six_words_returns_first_five_words():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""

def test_long_sentence_returns_first_five_and_dots():
    result = make_snippet("today I went to the shop and bought some milk.")
    assert result == "today I went to the..."