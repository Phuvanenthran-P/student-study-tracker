# 🎓 Student Study Tracker (Django)

A full-stack Django web application that helps students **plan, track, and analyze** their daily study progress across multiple subjects.

Built with authentication, relational data modeling, progress tracking, and production deployment in mind.

---

## 🚀 Features

* User authentication (Sign up / Login / Logout)
* Subject management (add your own subjects)
* Study plans with:

  * Daily target hours
  * Start & end dates
* Daily study logs
* Automatic progress calculation
* Clean, classic UI (no frontend frameworks)
* Secure deployment-ready configuration

---

## 🧠 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Django Templates)
* **Database:** SQLite (local) / PostgreSQL-ready
* **Auth:** Django built-in authentication
* **Deployment:** Render
* **Static Files:** WhiteNoise
* **Server:** Gunicorn

---

## 📂 Project Structure

```
student-study-tracker/
│
├── config/              # Project settings & URLs
├── tracker/             # Core application
│   ├── models.py        # Subject, StudyPlan, StudyLog
│   ├── views.py         # Business logic
│   ├── forms.py         # Django ModelForms
│   ├── urls.py
│   └── templates/
│       └── tracker/
│           ├── base.html
│           ├── dashboard.html
│           ├── form.html
│
├── templates/
│   └── auth/
│       ├── login.html
│       └── signup.html
│
├── staticfiles/
├── requirements.txt
├── manage.py
└── README.md
```

---

## ⚙️ Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/student-study-tracker.git
cd student-study-tracker
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Start development server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000`

---

## 🔐 Environment Variables

For production, set:

```
SECRET_KEY=your-secret-key
DEBUG=False
```

---

## 🌍 Deployment (Render)

**Build Command**

```
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

**Start Command**

```
gunicorn config.wsgi:application
```

---

## 📊 Core Models

* **Subject**
* **StudyPlan**
* **StudyLog**

Relations:

* One user → many subjects
* One subject → one study plan
* One plan → many study logs

---

## 🎯 What This Project Demonstrates

* Real Django MVC understanding
* Relational database design
* Authentication & authorization
* Form handling & validation
* Deployment knowledge (not just local apps)
* Clean, readable code structure

---

## 🔮 Future Improvements

* Weekly/monthly analytics
* Study streak tracking
* REST API (Django REST Framework)
* React frontend
* Notifications & reminders
* Role-based access (mentor/student)

---

## 🧑‍💻 Author

Built by **Phuvanenthran P**
Aspiring Python Developer | Django | Data Science Enthusiast

---

## 📜 License

This project is open-source and free to use for learning and portfolio purposes.
