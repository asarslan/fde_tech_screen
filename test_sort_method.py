import pytest
from sort_method import sort

class TestSortMethod:

    @pytest.mark.parametrize(
        "width, height, length, mass, expected", [
            (10, 10, 10, 5, 'STANDARD'),
            (100, 100, 100, 5, 'SPECIAL'),   
            (200, 10, 10, 5, 'SPECIAL'),     
            (10, 10, 10, 25, 'SPECIAL'),     
            (200, 10, 10, 25, 'REJECTED'),   
        ]
    )
    def test_sort_valid_cases(self, width, height, length, mass, expected):
        assert sort(width, height, length, mass) == expected

    @pytest.mark.parametrize(
        "width, height, length, mass, expected_exception", [
            (-10, 10, 10, 10, ValueError),
            (10, 10, 10, 0, ValueError),
            ("10", 10, 10, 10, TypeError),
        ]
    )
    def test_sort_invalid_inputs(self, width, height, length, mass, expected_exception):
        with pytest.raises(expected_exception):
            sort(width, height, length, mass)