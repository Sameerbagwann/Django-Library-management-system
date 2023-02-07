# Generated by Django 4.1.5 on 2023-01-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pdet', models.CharField(max_length=500)),
                ('cat', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created_on', models.DateTimeField()),
                ('image', models.CharField(max_length=10000)),
            ],
        ),
    ]