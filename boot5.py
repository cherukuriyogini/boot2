def subsets(nums):
    result = []

    def backtrack(index, current):
        # Store the current subset
        result.append(current[:])

        # Try adding remaining elements
        for i in range(index, len(nums)):
            current.append(nums[i])     # include element
            backtrack(i + 1, current)   # move to next index
            current.pop()               # remove element

    backtrack(0, [])
    return result