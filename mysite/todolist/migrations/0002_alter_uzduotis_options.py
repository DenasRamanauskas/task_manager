# Generated by Django 4.1.6 on 2023-02-10 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uzduotis',
            options={'ordering': ['-data'], 'verbose_name': 'Užduotis', 'verbose_name_plural': 'Užduotys'},
        ),
    ]
