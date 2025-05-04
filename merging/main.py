def merge_lists(ls1, ls2):
    merged_lists = ls1 + ls2
    for item in merged_lists:
        if not isinstance(item, (int, float)):
            raise TypeError("Lists can contain only integers or floats")

    return sorted(merged_lists)





print(merge_lists([1, 2, 4, 5], [6]))
# print(merge_lists([-3, 0], [-5, 2]))
# print(merge_lists([5, 1], [4, 2]))
print(merge_lists([1.5, 2], [3.1, -2, -2.7]))
# print(merge_lists([-30, -10, 0, 15, 16], [-20, -5, 5]))
# print(merge_lists([], []))
# print(merge_lists(["a", "d", 5, "p", "b"], ["c", 8, 5]))