FROM python:3.9

# make app dier
WORKDIR /app

# pip instarll
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy other code
COPY . .

# start app
CMD ["python", "sample.py"]
