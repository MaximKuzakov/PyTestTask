import pytest


#Type list testing
#Параметризованный тест
@pytest.mark.parametrize("lst, expected_len", [([1 , (2,), 3], 3),
                                               (['1', 2.0], 2),
                                               ([], 0)])
def test_list_func_len(lst, expected_len):
    assert len(lst) == expected_len, 'Unexpected function behavior'


#Негативный тест
def test_list_meth_indx():
    try:
        assert [1, 2, 3, 4, 5][5]
    except IndexError:
        pass


def test_list_meth_revers():
    lst = list(range(1, 100, 2))
    expected_result = list(range(99, -1, -2))
    lst.reverse()
    assert lst == expected_result, 'Unexpected methods behavior'


#Type tuple testing
#Параметризованный тест
@pytest.mark.parametrize("tpl, desired, expected_count", [((1, 2, 2, 3, 1, 2), 1, 2),
                                               (('1', '11', '', '1', '2', 'str'), '1', 2),
                                               (([2.0, 8.1, 3], [1], [1,1]), [1], 1)])
def test_tuple_meth_count(tpl, desired, expected_count):
    assert tpl.count(desired) == expected_count, 'Unexpected methods behavior'


#Негативный тест
def test_tuple_meth_indx():
    try:
        assert (1, 2.0, 3, '4', (5,)).index(-1)
    except ValueError:
        pass


def test_tuple_unpacking():
    a, b = 1, 10
    a, b = b, a
    assert a == 10 and b == 1, 'Unexpected unpacking behavior'