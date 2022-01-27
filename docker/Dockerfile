FROM ubuntu:20.04
WORKDIR /app
ENV LANG C.UTF-8
RUN apt update \
    && apt -y upgrade \
    && apt install -y iputils-ping \
    && apt install -y openssh-server \
    && apt install -y net-tools \
    && apt install -y python3-pip \
    && python3 --version \
    && pip3 --version
RUN useradd --user-group python \
    && mkdir -p /home/python \
    && chown -R python:python /home/python \
    && echo "python:python" > pass.txt \
    && chpasswd <pass.txt \
    && rm pass.txt
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
EXPOSE 22
ENTRYPOINT /entrypoint.sh
