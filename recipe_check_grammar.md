# Check Grammar FunctionDesign Recipe

## 1. Describe the problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation

Decisions:

Returns True or False
Suitable punctuations = . ! ?

## 2

def check_grammar(text):
#paramaters:
# text: string
#returns:
# bool - True if it starts with a capital AND ends with . ! or ?
#side effects:
# none

## 3. Examples
check_grammar("Hello there.") => True
check_grammar("hello there.") => False
check_grammar("Hello there") => False
check_grammar("Hello there!") => True
check_grammar("Hello there?") => True
check_grammar("Hello there.") => True

## 4 Implement the behavior
(done in lib/check_grammar.py, test by test)