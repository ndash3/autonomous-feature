# Generated by Django 4.2.9 on 2024-04-06 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=50)),
                ('feature_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PluggableDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PluggableRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_name', models.CharField(max_length=50)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='features.pluggabledatabase')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_status', models.BooleanField(default=False)),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdb_mapping', to='features.pluggabledatabase')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='features.featuresname')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdb_request', to='features.featuresname')),
            ],
        ),
    ]
