from flask import Flask, render_template_string, request, redirect
import mysql.connector

app = Flask(__name__)

# 資料庫連線函式
def get_db_connection():
    return mysql.connector.connect(
        host='mariadb',
        user='user',
        password='password',
        database='sampledb'
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 如果使用者按下「送出」按鈕 (POST)
    if request.method == 'POST':
        new_msg = request.form.get('message')
        if new_msg:
            cursor.execute("INSERT INTO test_table (message) VALUES (%s)", (new_msg,))
            conn.commit()
        return redirect('/')

    # 讀取所有資料 (GET)
    cursor.execute("SELECT message FROM test_table")
    rows = cursor.fetchall()
    conn.close()

    # 建立包含輸入框的 HTML
    html = """
    <html>
        <body>
            <h1>OpenShift 互動留言板</h1>
            <form method="POST">
                <input type="text" name="message" placeholder="輸入想hello hello 說的話..." required>
                <button type="submit">送出資料</button>
            </form>
            <hr>
            <h3>目前的資料庫內容：</h3>
            <ul>
                {% for row in rows %}
                    <li>{{ row[0] }}</li>
                {% endfor %}
            </ul>
        </body>
    </html>
    """
    return render_template_string(html, rows=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

