# Generated by Django 5.0.6 on 2024-05-31 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=10000)),
                ('url_uid', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Urls',
            },
        ),
    ]
