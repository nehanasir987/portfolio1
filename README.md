# Neha Nasir - Portfolio Website


 Home page:
![portfolio](https://github.com/user-attachments/assets/56f25643-7d70-4e55-9029-06e436b9051d)

 projects:
![Screenshot From 2025-06-28 00-20-56](https://github.com/user-attachments/assets/dc38aedf-55f6-4331-9726-fac521778d76)


A modern, responsive portfolio website built with Django, showcasing my skills, projects, and professional journey as a Full Stack Developer.

## Features:
- **Responsive Design**:     Works on all devices from mobile to desktop  
- **Modern UI**:             Clean, professional interface with animations  
- **Project Showcase**:      Display projects with images/videos and tech stacks  
- **Contact Form**:          Functional form with email integration  
- **Dynamic Content**:       Admin panel to manage all content  
- **Performance Optimized**: Fast loading with optimized assets

  
### Technologies Used:

## Frontend
- HTML5, CSS3, JavaScript  
- Bootstrap 5  
- Font Awesome Icons  
- Animate.css
## Backend
- Django (Python)  
- PostgreSQL (or SQLite for development)  
- Whitenoise (for static files)
  
### Development Tools
- Git & GitHub  
- VS Code  
- Chrome DevTools



## "Project Structure:"
portfolio/
├── static/ # All static files (CSS, JS, images)
│ ├── css/ # Stylesheets
│ ├── js/ # JavaScript files
│ └── images/ # Image assets
****
├── templates/ # HTML templates
│ ├── portfolio/ # App-specific templates
│ └── base.html # Base template
****
├── manage.py # Django management script
└── requirements.txt # Python dependencies



## Installation:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/nehanasir987/portfolio.git
   cd portfolio

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate                      ## On Windows: venv\Scripts\activate      ____________    ##on Linux:  venv/bin/activate

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt

6. **Run migrations**
    ```bash
   python manage.py migrate

8. **Create superuser (for admin access)**
    ```bash
    python manage.py createsuperuser

9. **Run development server**
    ```bash
    python manage.py runserver
   
