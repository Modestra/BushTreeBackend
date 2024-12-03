# Generated by Django 5.1.3 on 2024-12-02 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bushtree', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flowerdataset',
            name='description',
        ),
        migrations.AddField(
            model_name='flowerdataset',
            name='decorative_terms_end',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flowerdataset',
            name='decorative_terms_start',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flowerdataset',
            name='height_from',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flowerdataset',
            name='height_to',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flowerdataset',
            name='frost_resistance_zone',
            field=models.IntegerField(null=True),
        ),
    ]