# Generated by Django 5.0.2 on 2024-02-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='employee',
            table='mydatabase_employee',
        ),
    ]