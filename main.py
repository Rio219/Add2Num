#!/usr/bin/env python3
"""Interactive / Console Demo for MyBigNumber."""

import argparse
import logging
import sys
from pathlib import Path

# Thêm đường dẫn src vào sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from my_big_number import MyBigNumber


def main() -> None:
    # Cấu hình logging hiển thị trực tiếp ra màn hình console theo chuẩn
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    )

    parser = argparse.ArgumentParser(
        description="Demo chương trình cộng 2 số lớn theo giải thuật học sinh tiểu học (MyBigNumber)."
    )
    parser.add_argument("stn1", nargs="?", help="Số thứ nhất (chuỗi ký số)")
    parser.add_argument("stn2", nargs="?", help="Số thứ hai (chuỗi ký số)")
    args = parser.parse_args()

    adder = MyBigNumber()

    if args.stn1 is not None and args.stn2 is not None:
        stn1, stn2 = args.stn1, args.stn2
    else:
        # Nếu không truyền tham số qua dòng lệnh, demo ví dụ trong tài liệu
        print("=== CHẠY VÍ DỤ MẪU TỪ TÀI LIỆU YÊU CẦU ===")
        stn1, stn2 = "1234", "897"

    print(f"\nPhép tính: {stn1} + {stn2}\n")
    print("--- CÁC BƯỚC THỰC HIỆN (LOGGING) ---")
    result = adder.sum(stn1, stn2)
    print("-----------------------------------")
    print(f"\n=> KẾT QUẢ CUỐI CÙNG: {result}\n")


if __name__ == "__main__":
    main()
