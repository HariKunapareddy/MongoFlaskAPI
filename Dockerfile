#base image
FROM python:3.6

#set workdir

WORKDIR /tmp

#add the files to image
ADD FlaskAPI.py .
ADD MongoOperator.py .
ADD Requirement.txt .
ADD config.ini .
ADD Dockerfile .

RUN pip install -r Requirement.txt

CMD['python' , './FlaskAPI.py']