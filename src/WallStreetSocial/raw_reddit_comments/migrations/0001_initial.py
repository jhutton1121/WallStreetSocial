# Generated by Django 4.1 on 2022-09-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.TextField()),
                ('comment_body', models.TextField()),
                ('comment_upvotes', models.IntegerField()),
            ],
        ),
    ]
