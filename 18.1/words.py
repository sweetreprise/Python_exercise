def print_upper_words(words, must_start_with):
    """ takes in a list of words and capitalizes all of them that
    start with whatever is passed into must_start_with"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
