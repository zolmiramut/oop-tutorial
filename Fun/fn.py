def check_mirrored_array(input_list):
    """
    receive list/array and check if mirrored
    :return: true if mirrored else, false
    """
    end = -1
    midpoint = len(input_list) // 2
    for n in range(midpoint):
        if input_list[n] == input_list[end]:
            end = end - 1
            if n == midpoint - 1:
                return "true"

        else:
            return 'false'


arr1 = ['a', 'b', 'c', 'c', 'x', 'a']
arr2 = ['a', 'b', 'c', 'c', 'b', 'a']
arr3 = ['a', 'e', 'r', 'n', 'e', 'a']
print(check_mirrored_array(arr1))
print(check_mirrored_array(arr2))
print(check_mirrored_array(arr3))
