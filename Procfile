web: gunicorn application:app
web: pipenv run python src/manage.py runserver $PORT
web: gunicorn firsfurniturebot.wsgi:application --log-file - --log-level debug
web: gunicorn firsfurniturebot.wsgi --log-file -
web: gunicorn firsfurniturebot.wsgi
web: gunicorn firsfurniturebot.src.wsgi
