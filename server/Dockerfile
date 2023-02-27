FROM python:3.9
RUN python3 -m pip install flask transformers

EXPOSE 8000
COPY server_01.py ./server_01.py

CMD ["python", "server_01.py"]