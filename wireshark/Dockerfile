FROM python

WORKDIR /app
COPY . .

RUN pip3 install flask
RUN pip3 install flask-session

CMD [ "python3", "app.py" ]

EXPOSE 40009