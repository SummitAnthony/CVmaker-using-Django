# Generated by Django 5.0.1 on 2024-01-22 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvpdfconvert', '0002_remove_profile_degree_remove_profile_previous_work_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='language',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='project',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
