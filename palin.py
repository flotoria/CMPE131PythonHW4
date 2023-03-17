def palindrome(list):
    pointer1 = 0
    pointer2 = len(list) - 1

    while pointer1 < pointer2:
        if (list[pointer1] == list[pointer2]):
            pointer1 += 1
            pointer2 -= 1
        else:
            return False
    return True
