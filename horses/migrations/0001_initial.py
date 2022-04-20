# Generated by Django 4.0.3 on 2022-04-20 09:41

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
            name='Horse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('mother', models.CharField(max_length=64)),
                ('father', models.CharField(max_length=64)),
                ('birth_date', models.DateField()),
                ('age', models.SmallIntegerField()),
                ('stall', models.IntegerField()),
                ('owner', models.CharField(max_length=64)),
                ('picture', models.ImageField(upload_to='images')),
                ('farrier', models.ManyToManyField(related_name='f_horses', to=settings.AUTH_USER_MODEL)),
                ('vet', models.ManyToManyField(related_name='v_horses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HorseBits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VetAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='horses.horse')),
                ('vet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinesDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('horse', models.ManyToManyField(related_name='horses', to='horses.horse')),
                ('shot', models.ManyToManyField(related_name='vaccines', to='horses.vaccines')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.SmallIntegerField(choices=[(0, 'Choose a day'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=0)),
                ('description', models.TextField()),
                ('trainer', models.CharField(max_length=64)),
                ('duration', models.DurationField()),
                ('hour', models.TimeField()),
                ('horse', models.ManyToManyField(related_name='Trainings', to='horses.horse')),
                ('horse_bit', models.ManyToManyField(related_name='Trainings', to='horses.horsebits')),
            ],
        ),
        migrations.CreateModel(
            name='Stable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('stalls_quantity', models.IntegerField()),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='horses.horse')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.SmallIntegerField(choices=[(0, 'Choose a meal'), (1, 'Breakfast'), (2, 'Dinner'), (3, 'Supper')], default=0)),
                ('description', models.TextField()),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feeding_plans', to='horses.horse')),
            ],
        ),
        migrations.CreateModel(
            name='FarrierAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
                ('farrier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='horses.horse')),
            ],
        ),
    ]
