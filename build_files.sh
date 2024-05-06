echo "======> INSTALLING REQUIREMENTS <======"
pip3 install -r requirements.txt
echo "======> REQUIREMENTS INSTALLED <======"

echo "======> COLLECTING STATIC FILES <======"
python3 manage.py collectstatic --noinput --clear
echo "======> STATIC FILES COLLECTED <======"

echo "======> MAKE-MIGRATIONS <======"
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "======> MAKE-MIGRATIONS-END <======"
