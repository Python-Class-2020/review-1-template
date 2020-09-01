import main

def test_main():
    assert main.classify_students([3,9,7,2,1,5,11,4]) == [5,1,2]
    assert main.classify_students([1,2,3,4,5,6,7,8,9,10,11,12]) == [5,3,4]
    assert main.classify_students([7,2,9,3,8,10]) == [2,2,2]