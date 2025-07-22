# 📅 EventEase – Event Management System

EventEase is a full-stack Event Management System developed using **Python** and **Django**. This project was created as part of our **Second Year BSc (Hons) Computing** coursework at **Itahari International College**. It allows users to create, browse, search, and manage events and venues, with admin approval functionality and user authentication.

---

## 🚀 Features

- ✅ User registration and login
- 🎟️ Create and manage events
- 🏢 Add and manage venues
- 🔍 Search events and venues
- 🧾 List of events by venue
- 📋 View event details
- 🛡️ Admin approval for events
- 🧑 My Events dashboard for users
- ✏️ Edit/Update events and venues

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Custom styles)
- **Database**: SQLite3 (default for Django projects)
- **Templates**: Django templating engine

---

## 📁 Folder Structure (Simplified)

EventEase/
│
├── Events/ # Main app for event & venue management
│ ├── migrations/ # Database migrations
│ ├── static/css/ # CSS styling
│ ├── templates/Events/ # Event and venue templates
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── users/ # Handles user authentication
│ ├── migrations/
│ ├── templates/authenticate/
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ └── views.py
│
├── templates/ # Base and shared templates
│
├── db.sqlite3 # SQLite3 database
├── manage.py # Django project manager
└── README.md # Project documentation

yaml
Copy code

---



## 🔧 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ArynChd/EventEase.git
   cd EventEase

   
Create and activate a virtual environment:

python -m venv env
source env/bin/activate    # On Windows: env\Scripts\activate

Install the dependencies:
pip install -r requirements.txt

Apply migrations and run the server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

👨‍💻 Author
Aryan Chaudhary
BSc (Hons) Computing – Year 2
Itahari International College

