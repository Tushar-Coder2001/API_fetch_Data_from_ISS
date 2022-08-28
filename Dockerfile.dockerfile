
FROM python:3.8


ADD proj_1.py .
#ADD connection_mysql.py .
#Set up local sql in Docker
ADD location.py .
ADD temp.py .
ADD time_test_1.py .

RUN pip install --upgrade pip
RUN pip install python-csv
RUN pip install datetime
RUN pip install jsons
RUN pip install geograpy3
RUN pip install geopy
#RUN pip install mysql-connector-python

CMD ["python","./proj_1.py"]

