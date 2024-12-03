set -o errexit

pip install -r CHATBOT_CBAHI/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
