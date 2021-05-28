FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean

WORKDIR /opt/
RUN wget https://www.modbusdriver.com/downloads/diagslave.tgz
RUN tar xzf diagslave.tgz

COPY start.sh .
RUN chmod u+x start.sh

CMD ["./start.sh"]