FROM python:3.11-slim

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=web_server.py
ENV PIP_ROOT_USER_ACTION=ignore

ENV PATH="/home/myuser/.local/bin:${PATH}"

CMD ["python", "web_server.py"]
