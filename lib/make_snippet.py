
#split string into list of words
#check if more than 5 words
#slice the first 5 words
#join back with spaces
#5 or fewer return as is

def make_snippet(string):
    words = string.split()
    if len(words) > 5:
        first_five = words[:5]
        return " ".join(first_five) + "..."
    return string


