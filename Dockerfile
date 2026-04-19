FROM registry.access.redhat.com/ubi9/python-39

# 解決 Empty reply 的關鍵：禁用 Python 緩衝
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .
# 2. 這一行就會根據清單安裝 flask 和 mysql-connector-python
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
