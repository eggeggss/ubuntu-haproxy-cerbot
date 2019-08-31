
uwsgi --static-map /static=/srv/django/static
uwsgi --http :8080 --module myweb.wsgi
