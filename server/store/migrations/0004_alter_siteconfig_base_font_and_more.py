# Generated by Django 4.1.1 on 2022-11-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_testimonial_reviewer_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfig",
            name="base_font",
            field=models.CharField(
                default="Tahoma",
                help_text="Any valid <a href='https://fonts.google.com/' target='_blank'>Google Font name</a>. Dynamically loaded at runtime.",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="siteconfig",
            name="site_name_font",
            field=models.CharField(
                default="Pacifico",
                help_text="Any valid <a href='https://fonts.google.com/' target='_blank'>Google Font name</a>. Dynamically loaded at runtime.",
                max_length=100,
            ),
        ),
    ]
