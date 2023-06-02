FROM python:3.11.3
WORKDIR /app
RUN pip install uvicorn[standard] virtualenv fastapi pymongo python-dotenv
COPY . /app
CMD [ "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000" ]