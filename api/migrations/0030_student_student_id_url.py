# Generated by Django 5.1.2 on 2024-11-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_courses_course_obligatory_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_id_url',
            field=models.URLField(null=True),
        ),
    ]
