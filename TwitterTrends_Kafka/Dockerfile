FROM spotify/kafka
MAINTAINER "Israel Zúñiga de la Mora https://github.com/israelzuniga

# Install Python
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

# Install tweepy
RUN pip3 install  tweepy

# Install Kafka for python
RUN pip3 install kafka-python
