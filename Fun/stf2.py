def check_mirrored_array(input_list):
    """
    receive list/array and check if mirrored
    :return: true if mirrored else, false
    """
    midpoint = len(input_list) // 2
    return input_list[:midpoint - 1] == input_list[-1:-midpoint:-1]


arr2 = ['a', 'b', 'c', 'c', 'b', 'a']
print(check_mirrored_array(arr2))
x