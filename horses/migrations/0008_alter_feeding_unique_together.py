# Generated by Django 4.0.3 on 2022-04-25 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0007_feeding_date_created'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='feeding',
            unique_together={('horse', 'meal')},
        ),
    ]
