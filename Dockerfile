FROM python:3.7

ADD . .

RUN pip install coverage

CMD [ "python", "./src/CalculatorTests.py" ]