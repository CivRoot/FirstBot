web: gunicorn application:app
web: pipenv run python src/manage.py runserver $PORT
web: gunicorn firsfurniturebot.wsgi --log-file -
web: gunicorn --chdir firsfurniturebot firsfurniturebot.wsgi
