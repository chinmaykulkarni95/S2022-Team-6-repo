# Generated by Django 4.0.2 on 2022-04-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("circle", "0010_circlepolicycompliance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="circle",
            name="no_of_users",
            field=models.IntegerField(default=1),
        ),
    ]
