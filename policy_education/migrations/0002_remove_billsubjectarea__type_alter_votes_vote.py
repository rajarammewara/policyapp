# Generated by Django 4.1.3 on 2023-01-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billsubjectarea',
            name='_type',
        ),
        migrations.AlterField(
            model_name='votes',
            name='vote',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=255),
        ),
    ]
