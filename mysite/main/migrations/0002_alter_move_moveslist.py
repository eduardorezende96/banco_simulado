# Generated by Django 4.1.3 on 2022-12-11 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='moveslist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='move', to='main.moveslist'),
        ),
    ]