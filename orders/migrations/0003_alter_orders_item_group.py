# Generated by Django 3.2 on 2021-12-14 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ItemGroups', '0002_auto_20211214_1752'),
        ('orders', '0002_auto_20211214_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='item_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ItemGroups.itemgroups'),
        ),
    ]