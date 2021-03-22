from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("nr_views", models.IntegerField(default=0)),
                ("nr_likes", models.IntegerField(default=0)),
            ],
        ),
    ]