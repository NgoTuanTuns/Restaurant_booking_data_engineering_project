from flask import Flask, render_template_string, jsonify
from SendData import send_data
from GenerateData import generate_data
app = Flask(__name__)

# ============================================================
# 👉 HÀM BẠN SẼ TỰ THÊM LOGIC VÀO ĐÂY
# ============================================================
def book_table():
    """
    Hàm này được gọi mỗi khi người dùng bấm nút "Đặt bàn".
    Bạn có thể thêm logic thật ở đây, ví dụ:
    - Ghi vào database
    - Gửi email/SMS xác nhận
    - Gọi API bên thứ ba
    """
    data = generate_data()
    send_data(data)
    print("Đã nhận yêu cầu đặt bàn!")
    return {"status": "success", "message": "Đặt bàn thành công!"}


# ============================================================
# Giao diện web (HTML đơn giản, có 1 nút)
# ============================================================
HTML_PAGE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Đặt bàn nhà hàng</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: #f5f0e8;
            font-family: Arial, sans-serif;
        }
        .container { text-align: center; }
        button {
            padding: 16px 40px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            background: #c0392b;
            color: white;
            cursor: pointer;
        }
        button:hover { background: #a93226; }
        #result { margin-top: 20px; font-size: 16px; color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🍽️ Nhà hàng ABC</h1>
        <button onclick="bookTable()">Đặt bàn</button>
        <div id="result"></div>
    </div>

    <script>
        async function bookTable() {
            const res = await fetch('/book', { method: 'POST' });
            const data = await res.json();
            document.getElementById('result').innerText = data.message;
        }
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/book", methods=["POST"])
def book():
    result = book_table()  # gọi hàm Python của bạn
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)