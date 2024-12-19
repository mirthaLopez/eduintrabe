# Generated by Django 5.1.2 on 2024-11-18 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_remove_payment_form_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paypal_receipt_url',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_receipt_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]