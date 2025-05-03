import pytest
from merging.main import merge_lists
# example input 1:
# expected output 1:

# example input 2:
# expected output 2:

# test 1
def test_merge_returns_sorted_result():
    # arrange
    list1 = [2, 7]
    list2 = [3, 5, 1]
    expected = [1, 2, 3, 5, 7]
    # act
    result = merge_lists(list1, list2)
    # assert
    assert result == expected
    
# test 2
def test_raises_type_error_with_non_numeric_input():
    # Arrange():
    # arrange
    list1 = [2, 7, "a"]
    list2 = [3, 5, 1]
        
    # act & assert
    with pytest.raises(TypeError):
        merge_lists(list1, list2)
        
# test 3
def test_if_both_lists_are_empty():
    # arrange
    list1 = []
    list2 = []
    expected = []
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected

# test 4   
def test_if_list1_is_empty():
    # arrange
    list1 = []
    list2 = [3, 1]
    expected = [1, 3]
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected
    
# test 5
def test_if_list2_is_empty():
    # arrange
    list1 = [3, 1]
    list2 = []
    expected = [1, 3]
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected

# test 6
def test_if_lists_contain_negative_numbers():
    list1 = [-3, 0]
    list2 = [-5, 2]
    expected = [-5, -3, 0, 2]
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected

# test 7 
def test_if_numbers_are_floats_and_negative():
    # arrange
    list1 = [1.5, 2]
    list2 = [3.1, -2, -2.7]
    expected = [-2.7, -2, 1.5, 2, 3.1]
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected
# test 8
def test_merge_when_both_lists_have_duplicates():
    # arrange
    list1 = [2, 2]
    list2 = [2, 2]
    expected = [2, 2, 2, 2]
    # act 
    result = merge_lists(list1, list2)
    # assert
    assert result == expected
    
# test 9
def test_merge_with_int_and_float():
    list1 = [1, 2.2]
    list2 = [3.5, 0]
    expected = [0, 1, 2.2, 3.5]
    result = merge_lists(list1, list2)
    assert result == expected