def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    VOWELS = set('aeiou')
    lst = list(s)
    indices = []
    reversed_vowels = []
    count = 0

    for idx, letter in enumerate(lst):
        if letter.lower() in VOWELS:
            indices.append(idx)
            reversed_vowels.append(letter)
    
    reversed_vowels.reverse()

    for idx in indices:
        lst.pop(idx)
        lst.insert(idx, reversed_vowels[count])
        count += 1

    return "".join(lst)
    

