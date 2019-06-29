def check_mirrored_array(input_list):
    """
    receive list/array , and check if array is mirrored
    :return: true if mirrored , else false
    """

    # Input =['a','b','c','c','b','a'] return true
    # Input = ['a', 'b', 'c', 'c', 'x', 'a'] return false

    mid_point = len(input_list) // 2

    return input_list[:mid_point - 1] == input_list[-1:-mid_point:-1]


print(check_mirrored_array([1, 2, 3, 3, 0, 1]))
# help(check_mirrored_array)
