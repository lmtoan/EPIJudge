# Solving Journal

6/22
---
- Solved [4.9](epi_judge_python/is_number_palindromic.py) with brute-force.
    - Book answer suggests a few formula:
        - Number of digits = `log-10 (x) + 1` = `math.log(x) // math.log(10) + 1`
        - Last digit = `x % 10`
        - First digit = `x // 10**(n-1)`
        - Remember to keep the number of digits for remaining in the outer loop, decreasing by 2, to avoid cases with zeros in the inner numbers like 10022001.
- Solved [4.8](epi_judge_python/reverse_digits.py) with brute-force.
    - Book answer suggests a while loop where `res = res * 10 + remaining % 10` and `remaining = remaining // 10`, starting `res = 0 and remaining = abs(x)`
- Each problem should have 2 functions
    - `def solution_tl()` and `def solution_book()`
    - Note the runtime for each