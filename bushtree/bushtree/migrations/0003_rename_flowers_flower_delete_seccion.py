# Generated by Django 5.1.3 on 2024-11-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bushtree', '0002_alter_flowers_color_main_alter_flowers_color_other_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flowers',
            new_name='Flower',
        ),
        migrations.DeleteModel(
            name='Seccion',
        ),
    ]
