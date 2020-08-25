def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return left


print(search([1, 2, 3, 4, 5, 6, 8, 9, 11, 23, 45, 50], 0))
s = [1, 2, 3, 4]