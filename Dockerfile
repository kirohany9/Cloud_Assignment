FROM python:alpine
RUN pip install regex
RUN pip install nltk
WORKDIR /app
COPY . /app
CMD [ "python", "test.py" ]