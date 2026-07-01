from flask import Flask, render_template_string
from SendData import send_data
from GenerateData import generate_data

app = Flask(__name__)


def book_table():
    data = generate_data()
    send_data(data)
    print("Đã nhận yêu cầu đặt bàn!")
    return {"status": "success", "message": "Đặt bàn thành công!"}


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
    </style>
</head>
<body>
    <div class="container">
        <h1>🍽️ Nhà hàng ABC</h1>
        <form action="/book" method="POST">
            <button type="submit">Đặt bàn</button>
        </form>
    </div>
</body>
</html>
"""

RESULT_PAGE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Kết quả đặt bàn</title>
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
        .icon { font-size: 48px; }
        .message { font-size: 20px; margin: 16px 0; color: {{ color }}; }
        a {
            display: inline-block;
            margin-top: 12px;
            padding: 10px 24px;
            background: #c0392b;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }
        a:hover { background: #a93226; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">{{ icon }}</div>
        <div class="message">{{ message }}</div>
        <a href="/">Quay lại trang đặt bàn</a>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_PAGE)


@app.route("/book", methods=["POST"])
def book():
    try:
        result = book_table() 
        return render_template_string(
            RESULT_PAGE,
            icon="✅",
            message=result.get("message", "Đặt bàn thành công!"),
            color="#27ae60",
        )
    except Exception as e:
        return render_template_string(
            RESULT_PAGE,
            icon="❌",
            message=f"Đặt bàn thất bại: {e}",
            color="#c0392b",
        )


if __name__ == "__main__":
    app.run(debug=True)