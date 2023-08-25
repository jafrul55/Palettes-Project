# Palettes-Project
pip install -r requirements.txt
Set up the database:
python manage.py makemigrations
python manage.py migrate

Create a superuser for accessing the admin panel:
python manage.py createsuperuser
Run the development server:

python manage.py runserver
Access the project in your web browser: http://localhost:8000/

API Endpoints
/public-palettes/ - Browse public palettes without login.
/palettes/ - Manage user's own palettes (CRUD operations).
/favorites/ - Manage user's favorite palettes (CRUD operations).

Technologies Used
Django
Django REST framework

admin username: admin
password: 12345
