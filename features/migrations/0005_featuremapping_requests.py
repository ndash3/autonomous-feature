# Generated by Django 4.2.9 on 2024-04-07 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_remove_featuremapping_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuremapping',
            name='requests',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pdb_request', to='features.pluggablerequest'),
            preserve_default=False,
        ),
    ]
