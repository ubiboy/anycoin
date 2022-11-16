FROM python:3.9.0

WORKDIR /home/

RUN echo "t"

RUN git clone https://github.com/ubiboy/anycoin.git

WORKDIR /home/anycoin/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=anycoin.settings.deploy && python manage.py migrate --settings=anycoin.settings.deploy  && gunicorn anycoin.wsgi --env DJANGO_SETTINGS_MODULE=anycoin.settings.deploy --bind 0.0.0.0:8000"]