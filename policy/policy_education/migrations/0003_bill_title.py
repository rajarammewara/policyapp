# Generated by Django 4.1.3 on 2023-01-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy_education', '0002_remove_billsubjectarea__type_alter_votes_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='title',
            field=models.CharField(default='Bill', max_length=255),
            preserve_default=False,
        ),
    ]