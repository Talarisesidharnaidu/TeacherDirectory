# Generated by Django 4.1.4 on 2023-02-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0003_alter_teacherdetails_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherdetails',
            name='Room_Number',
            field=models.CharField(max_length=100),
        ),
    ]
