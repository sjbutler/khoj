# Generated by Django 4.2.5 on 2023-10-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0006_alter_localmarkdownconfig_input_files_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="localpdfconfig",
            name="input_files",
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name="localpdfconfig",
            name="input_filter",
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name="localplaintextconfig",
            name="input_files",
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name="localplaintextconfig",
            name="input_filter",
            field=models.JSONField(default=list, null=True),
        ),
    ]
