from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm


from .models import Project, Education, Certification  # 👈 Add these imports

def index(request):
    skills = [ 
    {"name": "HTML5", "icon": "fab fa-html5", "desc": "Clean & semantic markup, SEO friendly structure.", "level": 95},
    {"name": "CSS3", "icon": "fab fa-css3-alt", "desc": "Responsive layouts, Grid & Flexbox, modern styling.", "level": 90},
    {"name": "Bootstrap", "icon": "fab fa-bootstrap", "desc": "Responsive design, components, and utilities.", "level": 85},
    {"name": "Python / Django", "icon": "fab fa-python", "desc": "Backend development, REST API, ORM, secure apps.", "level": 80},
    {"name": "Git / GitHub", "icon": "fab fa-github", "desc": "Version control, collaboration, and project management.", "level": 75}
]


    
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    
    return render(request, 'portfolio/index.html', {
        "skills": skills,
        "educations": educations,
        "certifications": certifications
    })




def project(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project.html', {'projects': projects})




# portfolio/views.py

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # empty form after submission
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'success': success})






