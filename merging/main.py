def merge_lists(ls1, ls2):
    combined_lists = ls1 + ls2
    sorted_list = sorted(combined_lists)
    return sorted_list
print(merge_lists([1, 2, 4, 5], [6]))