web: daphne rtgraph.asgi:application --port $PORT --bind 0.0.0.0 -v2
graphworker: python3 manage.py runworker --settings=rtgraph.settings -v2