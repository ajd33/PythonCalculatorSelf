FROM python:3.8

ADD src /src

CMD ["python", "./src/CsvReaderTests.py"]

CMD ["python", "./src/CalculatorTests.py"]