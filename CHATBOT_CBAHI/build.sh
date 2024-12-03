set -o errexit

pip install -r CHATBOT_CBAHI/requirements.txt

python CHATBOT_CBAHI/manage.py collectstatic --no-input
python CHATBOT_CBAHI/manage.py migrate
if [[ $CREATE_SUPERUSER ]];
then
  python CHATBOT_CBAHI/manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi