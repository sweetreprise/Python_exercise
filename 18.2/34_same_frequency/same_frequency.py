def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    one = {}
    two = {}

    for num in str(num1):
        one[num] = one.get(num, 0) + 1
        
    for num in str(num2):
        two[num] = two.get(num, 0) + 1

    if one == two:
        return True
    else:
        return False