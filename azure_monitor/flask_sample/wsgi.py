
# WSGI entrypoint for gunicorn (no side effects, no app.run)

from azure_monitor.flask_sample.app import app  # this must resolve to your Flask instance
application = app
