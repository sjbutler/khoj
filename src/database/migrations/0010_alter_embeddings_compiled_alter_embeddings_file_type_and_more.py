# Generated by Django 4.2.5 on 2023-10-04 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0009_alter_embeddings_compiled_alter_embeddings_file_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="embeddings",
            name="compiled",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="embeddings",
            name="file_type",
            field=models.CharField(
                choices=[
                    ("image", "Image"),
                    ("pdf", "Pdf"),
                    ("plaintext", "Plaintext"),
                    ("markdown", "Markdown"),
                    ("org", "Org"),
                    ("notion", "Notion"),
                    ("github", "Github"),
                    ("conversation", "Conversation"),
                ],
                default="plaintext",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="embeddings",
            name="hashed_value",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="embeddings",
            name="raw",
            field=models.TextField(),
        ),
    ]
