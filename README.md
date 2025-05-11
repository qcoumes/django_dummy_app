# django-dummy-app

A simple django's app containing some models and some data for test purpose.

## Installation

1. Copy the `dummy_app` directory to your Django project.

2. Add `dummy_app` to `INSTALLED_APPS` in your settings

3. To load the data :

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py loaddata dummy_app/geography_data.json.zip
    ```
