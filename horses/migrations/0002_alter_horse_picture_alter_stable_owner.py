# Generated by Django 4.0.3 on 2022-04-22 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('horses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='picture',
            field=models.ImageField(default='images/my_stb_def.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='stable',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
