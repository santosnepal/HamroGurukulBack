# Generated by Django 3.0.5 on 2021-05-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210514_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='user_types',
            field=models.CharField(max_length=10),
        ),
    ]