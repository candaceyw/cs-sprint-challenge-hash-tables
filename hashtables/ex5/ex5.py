# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    files_dict = {}
    result = []
    for i in files:
        # take file paths and split at the last forward slash /
        split_path = i.split('/')

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
