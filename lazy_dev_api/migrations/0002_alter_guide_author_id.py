# Generated by Django 3.2.9 on 2021-11-18 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lazy_dev_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lazy_dev_api.user'),
        ),
    ]
