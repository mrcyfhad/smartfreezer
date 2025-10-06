FROM python:3.13-slim

WORKDIR /app

COPY src/ src/
COPY tests/ tests/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["python3", "src/demo.py"] # this line could be modified eg to CMD ["pytest", "tests/"]



