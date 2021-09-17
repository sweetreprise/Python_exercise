def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    import math

    new_phrase = phrase.lower().replace(" ", "")
    half_length = math.floor(len(new_phrase) / 2)
    
    for count in range(0, half_length):
        if new_phrase[count] != new_phrase[len(new_phrase) - count - 1]:
            return False
    return True
    