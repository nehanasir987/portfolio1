from django.db import models

from django.db import models

class Project(models.Model):
    pro_title = models.CharField(max_length=100)
    pro_icon = models.CharField(max_length=50, default="fas fa-briefcase")  
    created_on = models.DateField(null=True, blank=True)
    pro_image = models.ImageField(upload_to='projects_images/', null=True, blank=True)
    pro_video = models.FileField(upload_to='project_videos/', null=True, blank=True)   
    pro_desc = models.TextField()
    github_link = models.URLField()
    tech_stack = models.CharField(max_length=200)

    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]

    def __str__(self):
        return self.pro_title


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} - {self.institute}"



class Certification(models.Model):
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    description = models.TextField()
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.provider}"




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"



