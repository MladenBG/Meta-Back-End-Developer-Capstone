new terminal
python -m venv venv
venv\Scripts\activate
python -m pip install django
django-admin startproject littlelemon .


in manage.py folder
python manage.py startapp app

add 'app', to installed aps setings

python manage.py makemigrations
python manage.py migrate
mysql --version

mysql -u root -p
OR
mysql -u root -p --port=3307

CREATE DATABASE name;
SHOW DATABASES;
EXIT;


python manage.py createsuperuser


python manage.py runserver



create pip enviroment
new terminal
python -m pip install pipenv

in rootproject
pipenv install django mysqlclient
pipenv shell
python manage.py migrate
python manage.py runserver


APIS
in Capstone terminal

.\venv\Scripts\activate
pip install djangorestframework
python manage.py runserver



instal djoser open new terminal
python -m pip install djoser

python -m ensurepip --upgrade
if not instaled pip
python -m pip install --upgrade pip

setings

DJOSER = {
    "USER_ID_FIELD": "username"
}

instaled apps

'djoser',

rest framework

REST_FRAMEWORK = {
    # Authentication classes
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],

    # Permissions (default: allow any request)
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Pagination settings
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
unit testing IMPORTANT DELETE YOUR FILES FITH test.py TO TESt WORK!!!!! MLADEN VUKCEVIC
python manage.py test


python manage.py makemigrations
python manage.py migrate


add in settings 

'rest_framework.authtoken',








admin username: admin
admin password: 1981



IMPORTANT ONLY THIS TESTING INSOMNIA

username gogo
passford P12345678


 method POST
http://127.0.0.1:8000/api-token-auth/

{
  "username": "gogo",
  "password": "P12345678"
}
