from alpine:latest

RUN apk add python3-dev
RUN apk update pip3

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["del_service.py"]


EXPOSE 5000

