# Generated by Django 3.2 on 2021-12-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20211214_1821'),
        ('ItemGroups', '0005_delete_itemgroups'),
        ('Items', '0003_alter_items_item_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
