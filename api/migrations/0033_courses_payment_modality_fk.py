# Generated by Django 5.1.2 on 2024-12-03 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_payment_modality'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='payment_modality_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.payment_modality'),
        ),
    ]