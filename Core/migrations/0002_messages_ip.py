# Generated by Django 2.2.6 on 2019-11-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='ip',
            field=models.CharField(default=192, max_length=50),
            preserve_default=False,
        ),
    ]
