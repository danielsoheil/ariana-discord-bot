FROM ubuntu:22.04

RUN apt update -y
RUN apt install ffmpeg -y
RUN apt install python3-pip -y
RUN pip3 install pipenv

WORKDIR /app
COPY . .

RUN pipenv install

ENV DISCORD_TOKEN=MTA0MDc2OxxxxxxxxxxxxxxzNQ.GWxxsN.wRufxxxxxxxxxxxxxxxxxxxxxxxxxxxxkYg4VA
ENV ARIANA_TOKEN=G2xxxxxxxxxxSWY

ENTRYPOINT ["pipenv", "run", "python", "main.py"]