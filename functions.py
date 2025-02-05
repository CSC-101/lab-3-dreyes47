more = [x + 1 for x in [1, 2, 3, 4]]
print(more)

def square(n:int) -> int:
    return n * n
squares = [square(x) for x in [1, 2, 3, 4]]
print(squares)


def check(n:int) -> bool:
    return n > 2

answer1 = [x for x in range(5) if check(x)]
print(answer1)

def inc(m:int) -> int:
    return m + 1

answer2 = [inc(x) for x in range(5) if check(x)]
print(answer2)

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list

result = copy([4, 9, 2, 1])
print(result)

# Double the value of a number.
# Input: a number to be doubled
# Result: a number
def double(n:int) -> int:
    result = n * 2
    return result