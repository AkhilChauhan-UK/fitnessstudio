# Fitness Studio Booking API

This Django REST API lets clients view available fitness classes (like Yoga, Zumba, HIIT), book spots, and view their bookings.

---

## 🚀 Features

✅ View all upcoming fitness classes  
✅ Book a spot in a class  
✅ Retrieve all bookings for a specific email  

---

## 🏗️ Tech Stack

- Python 3.x
- Django
- Django REST Framework

---

3️⃣ Apply migrations

python manage.py makemigrations
python manage.py migrate

4️⃣ Create a superuser

python manage.py createsuperuser

5️⃣ Run the server

python manage.py runserver

🧪 API Endpoints
✅ View Classes

GET /classes
Returns: List of upcoming classes.

✅ Book a Class

POST /book
Body JSON:

json

{
  "class_id": 1,
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
Returns: Booking confirmation.

✅ Get Bookings
sql

GET /bookings?email=john@example.com
Returns: List of bookings for the provided email.

⚙️ Admin Panel
Visit:

arduino

http://127.0.0.1:8000/admin/
Login with your superuser credentials to manage classes and bookings.



