# Generated by Django 3.1 on 2020-10-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gimnazium', '0004_zamena_pub_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zamena',
            name='pub_data',
        ),
        migrations.AddField(
            model_name='zamena',
            name='how_lesson',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='zamena',
            name='predmet',
            field=models.CharField(choices=[('Русский язык', 'Русский язык'), ('Математика', 'Математика'), ('История', 'История')], default=('Русский язык', 'Русский язык'), max_length=100),
        ),
    ]
