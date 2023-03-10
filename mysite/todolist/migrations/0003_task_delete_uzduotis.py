# Generated by Django 4.1.6 on 2023-02-10 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0002_alter_uzduotis_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('text', models.CharField(help_text='Name/info of the task', max_length=200, verbose_name='Name')),
                ('tbd', models.DateTimeField(blank=True, null=True, verbose_name='Until')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'ordering': ['tbd'],
            },
        ),
        migrations.DeleteModel(
            name='Uzduotis',
        ),
    ]
