def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix