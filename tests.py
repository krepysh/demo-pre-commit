from main import binary_search

def test_short_list():
    target = 1
    nums = [1]
    assert binary_search(nums, target) == 0
def test_not_found():
    target = 2
    nums = [1]
    assert binary_search(nums, target) == -1
