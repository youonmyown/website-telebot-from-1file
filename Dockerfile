FROM python:3.9

RUN pip install flask telebot

WORKDIR /app

# COPY config.py /app/config.py
COPY site1.py /app/
COPY menu.txt /app/
COPY main.py /app/
COPY static /app/static
COPY templates /app/templates

VOLUME [ "main.txt" ]

EXPOSE 5000

CMD ["sh", "-c", "python main.py & python site1.py"]
