# Generated by Django 3.2 on 2021-04-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExaminationMalpractice', '0002_alter_user_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photograph',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
