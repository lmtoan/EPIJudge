from test_framework import generic_test


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


def reverse_tl(x):
    negative = (x < 0)
    x = abs(x) # Convert to positive
    
    res = 0
    if x < 10:
        res = x
    else:
        rev_arr = convert_number_to_array(x)
        # print(rev_arr)
        p = 0
        for i in range(len(rev_arr)-1, -1, -1):
            res += rev_arr[i] * 10**p
            p += 1
    
    if negative:
        return (-1)*res
    return res


def reverse_book(x):
    negative = (x < 0)
    res, remaining = 0, abs(x)

    '''
    1132
    0*10 + 1132%10 = 2
    2*10 + 113%10 = 2*10 + 3
    (2*10 + 3)*10 + 11%10 = 2*10**2 + 3*10 + 1
    (2*10**2 + 3*10 + 1)*10 + 1%10 = 2*10**3 + 3*10**2 + 10 + 1
    1/10 stop
    '''

    while remaining >= 1:
        res = res * 10 + remaining % 10
        remaining = remaining // 10

    if negative:
        return (-1)*res
    return res


def reverse(x):
    # Average running time: 5 us. Median running time: 5 us
    # return reverse_book(x) 
    # Average running time: 29 us. Median running time: 27 us
    return reverse_tl(x)
    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
