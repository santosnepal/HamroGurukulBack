# Generated by Django 3.0.5 on 2021-05-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='types',
            field=models.CharField(max_length=1),
        ),
    ]