def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if len(word) == 1:
        return True
    if word[low_index] == word[high_index]:
        chars_are_neighbors = high_index == low_index + 1
        length_is_odd_and_last_character = high_index - 1 == low_index + 1
        if chars_are_neighbors or length_is_odd_and_last_character:
            return True
        return is_palindrome_recursive(word, (low_index + 1), (
            high_index - 1))
    else:
        return False
