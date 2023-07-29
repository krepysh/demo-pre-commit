def binary_search(nums: list[int], target) -> int:
    # Return an index of element with value target in sorted list nums.
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high -low) //2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            high = mid-1
        else:
            low =mid+1
    return - 1
