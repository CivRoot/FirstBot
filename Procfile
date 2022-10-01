web: pipenv run python src/manage.py runserver $PORT
web: gunicorn application:app
web: gunicorn FirstBot.wsgi:application --log-file - --log-level debug
web: gunicorn FirstBot.wsgi --log-file -
web: gunicorn FirstBot.wsgi
web: gunicorn FirstBot.src.wsgi
