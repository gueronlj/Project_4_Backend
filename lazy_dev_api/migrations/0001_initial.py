# Generated by Django 3.2.9 on 2021-11-18 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('likes', models.IntegerField()),
                ('content', models.CharField(max_length=1024)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=128)),
                ('online', models.BooleanField()),
                ('collection', models.ManyToManyField(to='lazy_dev_api.Guide')),
            ],
        ),
        migrations.AddField(
            model_name='guide',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lazy_dev_api.user'),
        ),
    ]
