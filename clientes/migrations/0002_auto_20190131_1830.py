# Generated by Django 2.1.5 on 2019-01-31 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=5, max_digits=5),
        ),
    ]
