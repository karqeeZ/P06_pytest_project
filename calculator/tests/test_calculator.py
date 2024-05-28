from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    def test_subtract(self):
        # arrange
        a = 9876
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 8642
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 645
        b = 818
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 527610
        assert result == expected

    def test_divide(self):
        # arrange
        a = 999
        b = 111
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 9
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        cal = Calculator()

        # act & assert
        try:
            cal.divide(9,0)
        except ZeroDivisionError:
            pass