# Given an array of numbers, rearrange them in-place so that
# even numbers appear before odd ones.
#
# Example
# {
# "numbers": [1, 2, 3, 4]
# }
# Output:
#
# [4, 2, 3, 1]
# The order within the group of even numbers does not matter;
# same with odd numbers. So the following are also
# correct outputs: [4, 2, 1, 3], [2, 4, 1, 3], [2, 4, 3, 1].


def arrange_even_odd(numbers):
    j = -1
    for i in range(0, len(numbers)):
        if numbers[i] % 2 == 0:
            j += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

print(arrange_even_odd([2,1,3,4]))




