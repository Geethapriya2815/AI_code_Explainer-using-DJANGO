
# 🧠 AI Code Explainer using DJANGO

This is a web application that uses AI to explain Python code. Built with Django, it provides an intuitive interface where users can input code and receive explanations for better understanding.

## 🚀 Features

- 🌐 User login and authentication
- 📝 Enter and submit Python code
- 🤖 Get AI-generated explanations
- 📜 View history of previous explanations
- 📦 Django-based backend with template rendering

## 🛠️ Technologies Used

- Python 3.12
- Django 5.x
- HTML/CSS (for templates)
- SQLite3 (default Django DB)

## 📂 Project Structure

```

ai\_code\_explainer/
│
├── ai\_code\_explainer/       # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── explainer/               # Main app
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── templates/
│       ├── explainer/
│       │   ├── home.html
│       │   ├── explain.html
│       │   └── history.html
│       └── registration/
│           └── login.html
│
├── db.sqlite3               # Default database
└── manage.py                # Django command utility

````

## 🔧 How to Run

```bash
# Clone the repository
git clone https://github.com/Geethapriya2815/AI_code_Explainer-using-DJANGO.git
cd AI_code_Explainer-using-DJANGO

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
````

## 👤 Author

* Geethapriya S.L.

