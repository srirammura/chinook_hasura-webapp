# Generated by Django 2.2 on 2021-03-23 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210323_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='artistid',
            field=models.ForeignKey(db_column='ArtistId', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Artists'),
        ),
    ]