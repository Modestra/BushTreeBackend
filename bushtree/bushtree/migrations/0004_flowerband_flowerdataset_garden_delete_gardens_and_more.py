# Generated by Django 5.1.3 on 2024-11-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bushtree', '0003_rename_flowers_flower_delete_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlowerBand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mass', models.PositiveIntegerField()),
                ('flower_band', models.FileField(upload_to='media/flowerband/')),
            ],
        ),
        migrations.CreateModel(
            name='FlowerDataset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('frost_resistance_zone', models.IntegerField()),
                ('light', models.TextField(null=True)),
                ('watering', models.TextField(null=True)),
                ('color_main', models.TextField(null=True)),
                ('color_other', models.TextField(null=True)),
                ('expansion_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gardens', models.FileField(upload_to='media/garden/')),
            ],
        ),
        migrations.DeleteModel(
            name='Gardens',
        ),
        migrations.AddField(
            model_name='flower',
            name='boarding',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='care',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='cleaning_for_the_winter',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='decorative_terms_end',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='decorative_terms_start',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='flower_color',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='keeping',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='landing_place',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='leaf_color',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='reproduction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='shelter_for_the_winter',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='soil_requirements',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='storage_before_planting',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='use_in_landscape_design',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='flower',
            name='winter_hardiness',
            field=models.TextField(null=True),
        ),
    ]
