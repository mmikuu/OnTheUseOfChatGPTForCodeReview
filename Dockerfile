FROM python:3.9

ENV WORK_DIR /work
WORKDIR ${WORK_DIR}

RUN pip install -U \
        setuptools \
        pip && \
    pip install pipenv
RUN apt update -y
COPY ./requirements.txt ${WORK_DIR}/requirements.txt
COPY ./chatgpt_review ${WORK_DIR}/

RUN pip install -r requirements.txt

ENTRYPOINT ["python","-m", "main2_analyze"]