# Generated by Django 3.1.7 on 2022-03-23 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220323_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisments',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='advertisments',
            old_name='district_id',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='advertisments',
            old_name='status_id',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='district_id',
            new_name='district',
        ),
    ]
