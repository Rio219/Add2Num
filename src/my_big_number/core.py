"""Module MyBigNumber implements elementary school addition algorithm for large numbers."""

import logging
from typing import Callable, List, Optional

logger = logging.getLogger("MyBigNumber")


class MyBigNumber:
    """Core class for performing big number addition mimicking elementary school steps."""

    def __init__(self, step_listener: Optional[Callable[[str], None]] = None) -> None:
        """Initialize MyBigNumber with an optional step listener callback.

        Args:
            step_listener: A callable that accepts a step description string.
        """
        self.step_listener = step_listener
        self.history: List[str] = []

    def _log_step(self, message: str) -> None:
        """Record a step message to logger, internal history, and notify listener if present."""
        logger.info(message)
        self.history.append(message)
        if self.step_listener:
            self.step_listener(message)

    def sum(self, stn1: str, stn2: str) -> str:
        """Calculate the sum of two large number strings using elementary school addition.

        Traverses stn1 and stn2 from right to left, adds digits column-by-column along with
        carry, logs each step of calculation, and returns the resulting sum string.

        Args:
            stn1: First number string.
            stn2: Second number string.

        Returns:
            The sum of stn1 and stn2 as a string.
        """
        # Chuẩn hóa khoảng trắng cơ bản bám sát đề bài
        s1 = str(stn1).strip() if stn1 is not None else ""
        s2 = str(stn2).strip() if stn2 is not None else ""

        self.history.clear()

        len1 = len(s1)
        len2 = len(s2)
        max_len = max(len1, len2)

        result_chars: List[str] = []
        carry = 0
        step_index = 1

        # Duyệt đồng thời từ phải sang trái
        for i in range(max_len):
            idx1 = len1 - 1 - i
            idx2 = len2 - 1 - i

            digit1 = int(s1[idx1]) if idx1 >= 0 else 0
            digit2 = int(s2[idx2]) if idx2 >= 0 else 0

            # Tính tổng 2 kí số tại cột hiện tại
            col_sum = digit1 + digit2
            total = col_sum + carry

            digit_res = total % 10
            new_carry = total // 10

            # Xây dựng chuỗi kết quả tích lũy theo từng bước (được biểu diễn từ phải sang trái như ví dụ)
            result_chars.append(str(digit_res))
            current_result_display = "".join(reversed(result_chars))

            # Định dạng mô tả bước giải thích chi tiết
            if carry > 0:
                step_detail = (
                    f"Bước {step_index}: Lấy {digit1} cộng với {digit2} được {col_sum}. "
                    f"Cộng tiếp với nhớ {carry} được {total}. "
                    f'Lưu {digit_res} vào kết quả được kết quả mới là "{current_result_display}". '
                    f"Ghi nhớ {new_carry}."
                )
            else:
                step_detail = (
                    f"Bước {step_index}: Lấy {digit1} cộng với {digit2} được {total}. "
                    f'Lưu {digit_res} vào kết quả được kết quả mới là "{current_result_display}". '
                    f"Ghi nhớ {new_carry}."
                )

            self._log_step(step_detail)

            carry = new_carry
            step_index += 1

        # Nếu sau khi duyệt hết các chữ số mà vẫn còn nhớ
        if carry > 0:
            result_chars.append(str(carry))
            current_result_display = "".join(reversed(result_chars))
            final_step = (
                f"Bước {step_index}: Còn nhớ {carry}, lưu {carry} vào đầu kết quả "
                f'được kết quả cuối cùng là "{current_result_display}".'
            )
            self._log_step(final_step)

        final_result = "".join(reversed(result_chars))
        return final_result
