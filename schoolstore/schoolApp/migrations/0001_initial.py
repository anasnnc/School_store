# Generated by Django 4.2.5 on 2023-09-06 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cours_name', models.TextField()),
                ('dptid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolApp.department')),
            ],
        ),
    ]
