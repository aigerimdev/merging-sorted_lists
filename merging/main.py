def merge_lists(ls1, ls2):
    merged_lists = ls1 + ls2
    sorted_list = sorted(merged_lists)
    return sorted_list




# print(merge_lists([1, 2, 4, 5], [6]))
# print(merge_lists([-3, 0], [-5, 2]))
# print(merge_lists([5, 1], [4, 2]))
print(merge_lists([1.5, 2], [3.1, -2, -2.7]))
# print(merge_lists([-30, -10, 0, 15, 16], [-20, -5, 5]))
# print(merge_lists([0], [0]))
# print(merge_lists(["a", "d", 5, "p", "b"], ["c", 8, 5]))