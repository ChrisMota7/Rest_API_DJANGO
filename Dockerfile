FROM python:3.10.4-alpine3.15

RUN apt-get update && apt-get install -y tdsodbc unixodbc-dev
RUN echo "[FreeTDS]\n\
Description = FreeTDS unixODBC Driver\n\
Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so\n\
Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so\n\
" > /etc/odbcinst.ini

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements

COPY ./ ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]