FROM python:3
RUN git clone https://github.com/Oriel-Barroso/Examen.git
RUN pip install pip
RUN pip install parameterized
WORKDIR /Examen
CMD ["python3","-m","unittest"]
