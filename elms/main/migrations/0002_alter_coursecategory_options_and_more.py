# Generated by Django 5.0.1 on 2024-01-15 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': 'Course Categories'},
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='phone_no',
            new_name='phone_number',
        ),
    ]
