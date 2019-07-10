# Generated by Django 2.0 on 2018-01-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0006_auto_20180103_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=60)),
                ('Description', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=60)),
                ('Description', models.TextField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='securitycontrol',
            name='Layer',
            field=models.ManyToManyField(blank=True, to='editor.SecurityLayer'),
        ),
        migrations.AddField(
            model_name='l3operationalthreat',
            name='SecurityControl',
            field=models.ManyToManyField(blank=True, to='editor.SecurityControl'),
        ),
    ]
