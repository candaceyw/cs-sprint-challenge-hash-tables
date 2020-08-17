def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    # Loop the range of length
    for i in range(length):
        cur = (limit - weights[i])

        # check if current is in dict
        if cur in weight_dict:
            cur_index = weight_dict[cur]
            # return index and current index
            return i, cur_index

        else:
            # else set current weight to current index
            weight_dict[weights[i]] = i

    return None