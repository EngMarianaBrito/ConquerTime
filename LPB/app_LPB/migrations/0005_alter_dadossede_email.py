# Generated by Django 3.2.8 on 2021-10-16 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_LPB', '0004_dadossede_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadossede',
            name='email',
            field=models.TextField(null=True),
        ),
    ]
