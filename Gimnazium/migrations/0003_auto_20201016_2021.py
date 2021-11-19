# Generated by Django 3.1 on 2020-10-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnazium', '0002_auto_20201016_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamena',
            name='cabinet',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='zamena',
            name='lesson',
            field=models.CharField(choices=[('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], default=('5', '5'), max_length=2),
        ),
    ]