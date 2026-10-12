"""Unit tests for MyBigNumber elementary addition algorithm."""

import sys
import unittest
from pathlib import Path

# Add src directory to sys.path to allow running tests from root
src_path = str(Path(__file__).resolve().parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):
    """Test suite covering various test cases and scenarios for MyBigNumber."""

    def setUp(self) -> None:
        self.adder = MyBigNumber()

    def test_example_from_requirement_pdf(self) -> None:
        """Test the exact case provided in the requirements: sum('1234', '897') = '2131'."""
        result = self.adder.sum("1234", "897")
        self.assertEqual(result, "2131")
        # Kiểm tra lịch sử các bước được ghi nhận
        self.assertGreater(len(self.adder.history), 0)
        self.assertTrue(any("Lấy 4 cộng với 7" in step for step in self.adder.history))
        self.assertTrue(any("Lấy 3 cộng với 9" in step for step in self.adder.history))

    def test_equal_length_without_carry(self) -> None:
        """Test two numbers of same length with no carry at any step."""
        result = self.adder.sum("123", "456")
        self.assertEqual(result, "579")

    def test_equal_length_with_carries(self) -> None:
        """Test two numbers of same length producing multiple carries."""
        result = self.adder.sum("587", "425")
        self.assertEqual(result, "1012")

    def test_cascade_carry(self) -> None:
        """Test cascade carry across multiple positions (e.g. 999999 + 1 = 1000000)."""
        result = self.adder.sum("999999", "1")
        self.assertEqual(result, "1000000")

    def test_add_with_zero(self) -> None:
        """Test adding with zero."""
        self.assertEqual(self.adder.sum("0", "0"), "0")
        self.assertEqual(self.adder.sum("12345", "0"), "12345")
        self.assertEqual(self.adder.sum("0", "98765"), "98765")

    def test_very_unequal_lengths(self) -> None:
        """Test numbers with significantly different lengths."""
        result = self.adder.sum("1", "99999999999999999999")
        self.assertEqual(result, "100000000000000000000")

    def test_large_numbers_comparison_with_python_int(self) -> None:
        """Test random-like very large numbers against Python native arbitrary precision."""
        num1 = "9876543210987654321098765432109876543210"
        num2 = "1234567890123456789012345678901234567890"
        expected = str(int(num1) + int(num2))
        self.assertEqual(self.adder.sum(num1, num2), expected)

    def test_whitespace_handling(self) -> None:
        """Test that leading/trailing whitespaces are properly stripped."""
        result = self.adder.sum("  1234 ", " 897  ")
        self.assertEqual(result, "2131")

    def test_step_listener_callback(self) -> None:
        """Test that the step_listener callback receives every recorded step."""
        captured_steps = []
        custom_adder = MyBigNumber(step_listener=lambda s: captured_steps.append(s))
        result = custom_adder.sum("12", "8")

        self.assertEqual(result, "20")
        self.assertEqual(len(captured_steps), 2)
        self.assertEqual(captured_steps, custom_adder.history)


if __name__ == "__main__":
    unittest.main()
