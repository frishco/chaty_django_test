# Generated by Django 2.2.7 on 2019-11-10 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=32)),
                ('avatar_url', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('type', models.CharField(max_length=64)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='RestAPI.Actor')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestAPI.Repository')),
            ],
        ),
    ]
