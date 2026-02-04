FROM python:3.11-slim

#write stdout/stderr immediatelly
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends tzdata \
    &&  rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

# default command, can be overwritten by compose
CMD ["python", "-m", "app.main"]