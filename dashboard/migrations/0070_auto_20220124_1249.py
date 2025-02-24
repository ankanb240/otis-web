# Generated by Django 3.2.9 on 2022-01-24 17:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0069_alter_pset_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palacecarving',
            name='student',
        ),
        migrations.AddField(
            model_name='palacecarving',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='User who owns this achievement', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
