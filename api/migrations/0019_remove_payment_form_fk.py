# Generated by Django 5.1.2 on 2024-11-18 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_payment_form_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='form_fk',
        ),
    ]
