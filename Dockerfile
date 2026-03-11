FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [&quot;gunicorn&quot;, &quot;--bind&quot;, &quot;0.0.0.0:5000&quot;, &quot;app:app&quot;]
