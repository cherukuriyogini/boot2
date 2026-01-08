def rearrangeArray(nums):
    positives = []
    negatives = []

    # Separating positives and negatives
    for num in nums:
        if num > 0:
            positives.append(num)
        else:
            negatives.append(num)

    result = []
    
    # Merging them alternately starting with positive
    for i in range(len(positives)):
        result.append(positives[i])
        result.append(negatives[i])

    return result
