# Multi-Organization Management System

A Django-based web application for managing users and organizations, with personalized dashboards, user authentication, and a clean frontend interface.

## 🚀 Features

- User authentication (login/logout)
- Role-based dashboards
- Organization assignment to users
- Customizable user profile view
- Styled frontend using custom CSS
- Admin panel for managing users and organizations

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS (custom static files), Bootstrap (optional)
- **Database**: SQLite (default), can be upgraded to PostgreSQL
- **Template Engine**: Django Templates
- **Admin Interface**: Django Admin

---

## 📁 Project Structure

multi_org_management_project/
│
├── manage.py
├── multi_org_management/ # Project settings
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── users/ # App to manage user-related logic
│ ├── views.py
│ ├── urls.py
│ ├── templates/users/
│ │ └── dashboard.html
│ └── ...
│
├── organizations/ # App to manage organizations
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
│
├── templates/ # Global templates
│ └── base_generic.html
│
├── static/ # Global static files
│ └── organization/
│ └── css/
│ └── style.css # Custom CSS
└── ...


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi_org_management_project.git
cd multi_org_management_project

2. Install dependencies

Make sure you have Python 3.10+ and Django installed:

pip install -r requirements.txt

If requirements.txt is missing, manually install Django:

pip install django

3. Create the static directory (if not present)

mkdir -p static/organization/css

Then add your custom styles to static/organization/css/style.css.
4. Run migrations

python manage.py makemigrations
python manage.py migrate

5. Create a superuser (admin)

python manage.py createsuperuser

6. Run the development server

python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
📄 Key Pages

    /login/ – User login

    /dashboard/ – User dashboard after login

    /organizations/ – Organization list or management

    /users/ – List of users (admin view)

    /admin/ – Django admin panel
