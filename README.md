After pull open terminal and write:

virtualenv -p python3 envname

source envname/bin/activate

pip install -r > requirements.txt

cd TestTask

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
