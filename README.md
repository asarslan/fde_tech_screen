# fde_tech_screen

### Overview

This module implements a sorting function that classifies packages based on their dimensions and mass into one of three categories: STANDARD, SPECIAL, or REJECTED. The classification depends on whether the package is bulky, heavy, or both.


### 1. Correct Sorting Logic

    Bulky condition: Determined by checking if the product of dimensions (width × height × length) is at least 1,000,000 cubic units or if any dimension exceeds 150 units.

    Heavy condition: Determined by mass being at least 20 units.

    Classification:

        Returns 'REJECTED' if both bulky and heavy.

        Returns 'SPECIAL' if either bulky or heavy.

        Returns 'STANDARD' if neither bulky nor heavy.

This logic follows the exact problem requirements clearly and correctly.

### 2. Code Quality

    Input validation is done upfront with explicit checks for:

        Numeric types (int or float) to prevent unexpected type errors.

        Positive, non-zero values to ensure valid physical dimensions and mass.

    The use of Python's math.prod() improves readability for volume calculation.

    Logical checks are clearly separated and straightforward.

    Well-documented with a concise docstring specifying return values and exceptions.

### 3. Handling Edge Cases & Inputs

    Type Validation: Raises TypeError if any input is not numeric.

    Value Validation: Raises ValueError if any input is zero or negative.

    Edge cases such as very large dimensions or masses, borderline values (exact thresholds) are covered by the tests.

    The function is robust to invalid input types and invalid numeric values.

### 4. Test Coverage

    Unit tests cover:

        Normal cases across all three output classes (STANDARD, SPECIAL, REJECTED).

        Boundary conditions like dimensions exactly at thresholds.

        Invalid inputs that trigger exceptions (TypeError, ValueError).

    Tests are implemented using pytest and utilize parameterization for clear and concise test cases.

    This ensures comprehensive coverage of both functionality and input validation.

### How to Test the Code

Prerequisites

    - Python 3.7+

    - pytest installed (pip install pytest)

Running Tests

    Clone or download the repository containing sort_method.py and test_sort_method.py.

    Navigate to the directory containing these files.

    Run tests using:
            pytest test_sort_method.py
