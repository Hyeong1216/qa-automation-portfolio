# 테스트 대상 함수들 (실제로는 별도 파일에 있겠지만 일단 같이 작성)

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# 테스트 함수들

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5),
    (100, 200, 300),
    (-10, 10, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected


@pytest.fixture
def sample_numbers():
    return {"a": 10, "b": 5}

def test_add_with_fixture(sample_numbers):
    assert add(sample_numbers["a"], sample_numbers["b"]) == 15

def test_divide_with_fixture(sample_numbers):
    assert divide(sample_numbers["a"], sample_numbers["b"]) == 2.0