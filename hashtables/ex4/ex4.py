def has_negatives(a):
    """
    YOUR CODE HERE
    """
    list_dict = {}
    result = []

    for i in a:
        if i not in list_dict:
            list_dict[i] = 1

    # check for negatives
    for num in list_dict:
        # formula to find neg opposite
        negative = num * -1
        # if it's matches positive, then add to result
        if negative in list_dict:
            if num > 0:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
