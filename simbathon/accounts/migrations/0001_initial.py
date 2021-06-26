# Generated by Django 3.2.4 on 2021-06-26 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=20)),
                ('job', models.CharField(choices=[('학생', '학생'), ('강사', '강사')], max_length=2)),
                ('school', models.CharField(default='', max_length=30)),
                ('grade', models.CharField(default='', max_length=30)),
                ('school_id', models.CharField(default='', max_length=30)),
                ('interests', models.CharField(default='', max_length=30)),
                ('service_hour', models.ImageField(default=0, upload_to='')),
                ('admin_approved', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profile',
                'db_table': 'user_profile',
                'ordering': ['id'],
            },
        ),
    ]
