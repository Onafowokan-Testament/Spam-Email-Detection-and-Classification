FROM python:3.11

WORKDIR /APP

COPY ./requirements.txt /APP/requirements.txt
COPY app.py /APP/app.py
COPY model.pkl /APP/model.pkl
COPY pipeline.pkl /APP/pipeline.pkl
COPY text_processing.py /APP/text_processing.py

EXPOSE 80

RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]