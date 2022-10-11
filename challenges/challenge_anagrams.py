def is_anagram(first_string, second_string):
    if (len(first_string) != len(second_string)):
        return False
    list_first_string = list(first_string.upper())
    list_second_string = list(second_string.upper())
    for letter in list_first_string:
        qnt_letter = list_first_string.count(letter)
        if (qnt_letter != list_second_string.count(letter)):
            return False
    return True