from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import base64

from django.http import HttpResponse
from django.template import loader



def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")

        address = request.POST.get("address", "")
        linkedin_url = request.POST.get("linkedin_url", "")
        github_url = request.POST.get("github_url", "")
        website_url = request.POST.get("website_url", "")
        education = request.POST.get("education", "")
        experience = request.POST.get("experience", "")
        skills = request.POST.get("skills", "")
        projects = request.POST.get("projects", "")
        certifications = request.POST.get("certifications", "")
        languages = request.POST.get("languages", "")
        interests = request.POST.get("interests", "")

        # Handle image file upload
        profile_image = request.FILES.get("profile_image")

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            address=address,
            linkedin_url=linkedin_url,
            github_url=github_url,
            website_url=website_url,
            education=education,
            experience=experience,
            skills=skills,
            projects=projects,
            certifications=certifications,
            languages=languages,
            interests=interests,
            profile_image=profile_image
        )
        profile.save()

        # Redirect the user to the resume view, passing the profile id
        return redirect('resume', id=profile.id)

    return render(request, 'cvpdfconvert/accept.html')





# ...



def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvpdfconvert/resume.html')

    # Read and encode the profile image
    with open(user_profile.profile_image.path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Include the encoded image in the HTML
    html = template.render({'user_profile': user_profile, 'encoded_image': encoded_image})

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    # Check if the URL contains 'download' to determine if it's a download request
    is_download = 'download' in request.path

    if is_download:
        # Download as PDF
        pdf = pdfkit.from_string(html, False, options)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    else:
        # View as HTML
        response = HttpResponse(html)

    return response


def download_resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvpdfconvert/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'cvpdfconvert/list.html', {'profiles':profiles})