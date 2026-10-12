# Add2Num - Thuật Toán Cộng 2 Số Lớn (Elementary Big Number Addition)

Dự án cài đặt thuật toán cộng hai số nguyên lớn được biểu diễn dưới dạng chuỗi kí tự theo phương pháp cộng từng cột như học sinh tiểu học (lớp 3).

## 1. Yêu cầu & Thiết kế
- **Class**: `MyBigNumber`
- **Method**: `sum(stn1: str, stn2: str) -> str`
- **Nguyên lý hoạt động**:
  1. Duyệt đồng thời chuỗi `stn1` và `stn2` từ phải sang trái (hàng đơn vị, hàng chục, hàng trăm...).
  2. Lấy ra từng kí tự, chuyển thành chữ số (digit) và thực hiện phép cộng kèm theo biến nhớ (`carry`).
  3. Ghi nhận chi tiết từng bước thông qua hệ thống `logging` tiêu chuẩn hoặc callback `step_listener` để phục vụ hiển thị trên giao diện (UI) hoặc ứng dụng console.

### Ví dụ minh họa (từ tài liệu đặc tả)
Với phép tính `sum("1234", "897")`:
- **Bước 1**: Lấy 4 cộng với 7 được 11. Lưu 1 vào kết quả được kết quả mới là `"1"`. Ghi nhớ 1.
- **Bước 2**: Lấy 3 cộng với 9 được 12. Cộng tiếp với nhớ 1 được 13. Lưu 3 vào kết quả được kết quả mới là `"31"`. Ghi nhớ 1.
- **Bước 3**: Lấy 2 cộng với 8 được 10. Cộng tiếp với nhớ 1 được 11. Lưu 1 vào kết quả được kết quả mới là `"131"`. Ghi nhớ 1.
- **Bước 4**: Lấy 1 cộng với 0 được 1. Cộng tiếp với nhớ 1 được 2. Lưu 2 vào kết quả được kết quả mới là `"2131"`. Ghi nhớ 0.
- **Kết quả cuối cùng**: `"2131"`

---

## 2. Cấu trúc thư mục (Directory Structure)

Thư mục dự án tuân theo đúng quy ước trong đề bài:
```text
~/Projects/github.com/riohoang/Add2Num
├── .gitignore
├── main.py                     # Demo ứng dụng Console
├── README.md                   # Hướng dẫn chi tiết
├── requirements.txt            # Danh sách dependencies (pytest)
├── src/                        # Thư mục mã nguồn chính (core)
│   └── my_big_number/
│       ├── __init__.py
│       └── core.py             # Lớp MyBigNumber
└── tests/                      # Thư mục Unit Testing độc lập
    └── test_my_big_number.py   # Bộ test case kiểm thử toàn diện
```

---

## 3. Hướng dẫn cài đặt & Thực thi

### 3.1. Yêu cầu môi trường
- Python 3.10 trở lên.
- Git.

### 3.2. Cài đặt môi trường ảo (Virtual Environment)
```bash
# Tạo môi trường ảo
python3 -m venv .venv

# Kích hoạt môi trường ảo
# Trên Linux/macOS:
source .venv/bin/activate
# Trên Windows:
# .venv\Scripts\activate

# Cài đặt thư viện test (tùy chọn)
pip install -r requirements.txt
```

### 3.3. Chạy chương trình Console Demo
Bạn có thể chạy thử nghiệm trực tiếp thông qua file `main.py`:

- Chạy với ví dụ mặc định trong đề bài:
  ```bash
  python3 main.py
  ```

- Chạy với 2 số bất kỳ:
  ```bash
  python3 main.py 99999999999999999999 1
  ```

---

## 4. Chạy Unit Testing (Kiểm thử)

Bạn có thể chạy kiểm thử bằng 1 trong 2 cách:

### Cách 1: Sử dụng thư viện chuẩn `unittest` (Không cần cài thêm thư viện)
```bash
python3 -m unittest discover -s tests -v
```

### Cách 2: Sử dụng `pytest`
```bash
pytest -v
```

### Các kịch bản kiểm thử (Test Scenarios Covered)
1. **Ví dụ chuẩn của đề bài**: Kiểm tra `1234 + 897 = 2131` và kiểm tra chi tiết các bước được ghi nhận đầy đủ.
2. **Hai số cùng độ dài không có nhớ**: `123 + 456 = 579`.
3. **Hai số cùng độ dài có nhớ ở bước cuối**: `587 + 425 = 1012`.
4. **Nhớ lan truyền liên tiếp (Cascade Carry)**: `999999 + 1 = 1000000`.
5. **Cộng với số 0**: `0 + 0 = 0`, `12345 + 0 = 12345`.
6. **Hai số chênh lệch độ dài lớn**: `1 + 99999999999999999999 = 100000000000000000000`.
7. **Số cực lớn hàng trăm chữ số**: Đối chiếu kết quả với phép cộng số nguyên lớn mặc định của Python.
8. **Xử lý khoảng trắng**: Tự động loại bỏ whitespace thừa nếu có.
9. **Cơ chế Callback / Listener**: Đảm bảo listener bên ngoài nhận được chính xác từng bước tính toán.

---

## 5. Tích hợp cho nhóm khác (API Integration)

Các nhóm phát triển giao diện (UI) hoặc ứng dụng mở rộng có thể sử dụng lớp `MyBigNumber` như sau:

```python
from my_big_number import MyBigNumber

# 1. Khởi tạo đối tượng
adder = MyBigNumber()

# 2. Gọi hàm cộng
result = adder.sum("1234", "897")
print(f"Tổng: {result}")

# 3. Lấy lại lịch sử các bước đã thực hiện
for step in adder.history:
    print(step)

# 4. Hoặc truyền callback lắng nghe từng bước trực tiếp (dùng cho Animation trên UI)
def on_step_calculated(step_text: str):
    print("UI update:", step_text)

live_adder = MyBigNumber(step_listener=on_step_calculated)
live_adder.sum("99", "1")
```

---

## 6. Phiên bản & Tag
- Phiên bản phát hành: `0.0.1`
- Git Tag: `v0.0.1` (hoặc `0.0.1`)
