FROM python:2.7

RUN pip install paho-mqtt

ADD dash_tcp_server.py /
 
EXPOSE 443

CMD [ "python", "./dash_tcp_server.py" ]


