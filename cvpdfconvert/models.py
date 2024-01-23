from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    summary = models.TextField(max_length=2000, blank=True)
    address = models.CharField(max_length=300, blank=True)
    linkedin_url = models.URLField(max_length=300, blank=True)
    github_url = models.URLField(max_length=300, blank=True)
    website_url = models.URLField(max_length=300, blank=True)
    education = models.TextField(max_length=2000, blank=True)
    experience = models.TextField(max_length=2000, blank=True)
    skills = models.TextField(max_length=2000, blank=True)
    projects = models.TextField(max_length=2000, blank=True)
    certifications = models.TextField(max_length=2000, blank=True)
    languages = models.CharField(max_length=300, blank=True)
    interests = models.CharField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name
