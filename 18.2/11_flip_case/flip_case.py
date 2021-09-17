def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lower = to_swap.lower()
    new_phrase = ''

    for letter in phrase:
        if lower == letter.lower():
            letter = letter.swapcase()
        new_phrase += letter

    return new_phrase