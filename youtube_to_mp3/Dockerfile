FROM python:3.9-slim-buster

# //// creating new user and setting workdir ///////////
ENV USER appuser
RUN useradd --create-home --shell /bin/bash ${USER}

USER ${USER}
WORKDIR /home/${USER}
# //////////////////////////////////////////////////////

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install moviepy

COPY . .
ENTRYPOINT [ "python", "-u", "main.py" ]