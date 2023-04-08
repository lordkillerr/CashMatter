# Generated by Django 4.2 on 2023-04-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('owes', models.JSONField(blank=True, default=dict, null=True)),
                ('owed_by', models.JSONField(blank=True, default=dict, null=True)),
            ],
        ),
    ]