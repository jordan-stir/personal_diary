from lib.check_grammar import *

def test_capital_and_full_stop_returns_true():
    result = check_grammar("Hello there.")
    assert result == True

def test_no_capital_returns_false():
    result = check_grammar("hello there.")
    assert result == False

def test_has_capital_no_punctuation():
    result = check_grammar("Hello there")
    assert result == False 

def test_exclamation_returns_true():
    result = check_grammar("Hello there!")
    assert result == True

def test_question_mark_is_true():
    result = check_grammar("Hello there?")
    assert result == True