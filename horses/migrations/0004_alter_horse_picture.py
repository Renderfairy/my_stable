# Generated by Django 4.0.3 on 2022-04-22 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0003_alter_horse_farrier_alter_horse_vet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='picture',
            field=models.ImageField(default='images/my_stb_def.jpg', null=True, upload_to='images'),
        ),
    ]
