# Generated by Django 4.1 on 2023-10-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_course_alter_students_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='courses2',
            field=models.ManyToManyField(blank=True, related_name='students2', to='myapp1.course'),
        ),
    ]
