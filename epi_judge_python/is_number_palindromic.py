from test_framework import generic_test
import math


def convert_number_to_array(x):
    # Convert to an array - O(n) time, O(n) space
    x = abs(x) # Convert to positive
    arr = [x%10]
    p = 2
    while x / 10**p >= 0.1:
        digit = (x % 10**p - x % 10**(p-1)) / 10**(p-1)
        arr.append(int(digit))
        p += 1
    return arr


def check_palin_array(arr):
    # Check if array is palindromic
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_number_tl(num):
    if num is None or num < 0:
        return False
    if num > 0 and num < 1:
        return False # fractions
    if num < 10:
        return True # single digit
    rev_arr = convert_number_to_array(num)
    return check_palin_array(rev_arr)


def is_palindrome_number_book(num):
    if num is None or num < 0:
        return False
    if num > 0 and num < 1:
        return False # fractions
    if num < 10:
        return True # single digit
    remaining = abs(num)
    n = math.floor(math.log10(remaining)) + 1
    while remaining > 0:
        last_digit = remaining % 10
        first_digit = remaining // 10**(n-1)
        if last_digit != first_digit:
            return False
        remaining = (remaining - first_digit * 10**(n-1) - last_digit) // 10
        n = n - 2
    return True


def is_palindrome_number(num):
    # Average running time: 5 us. Median running time: 5 us
    # O(n) time, O(1) space
    return is_palindrome_number_book(num)
    # Average running time: 13 us. Median running time: 9 us
    # return is_palindrome_number_tl(num)


if __name__ == '__main__':
    print(is_palindrome_number(1002002001))
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
