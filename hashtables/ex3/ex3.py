def intersection(arrays):
    """
    YOUR CODE HERE
    """
    list_dict = {}
    result = []

    for i in arrays:
        for num in i:
            # if num not in dict, add it.
            if num not in list_dict:
                list_dict[num] = 1
            else:
                result.append(num)

    # fromkeys() will return a dictionary with the result
    return list(dict.fromkeys(result))
    # return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
