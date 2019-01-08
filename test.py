from calculation import numbers_sum

def test_numbers_sum():
    assert numbers_sum(num1=2, num2=3) == 5
    return "testing_numbers_sum() passed successfully"
print test_numbers_sum()