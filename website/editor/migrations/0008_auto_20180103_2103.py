# Generated by Django 2.0 on 2018-01-03 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0007_auto_20180103_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityPerimeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=60)),
                ('Description', models.TextField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='l3operationalthreat',
            name='SecurityControl',
            field=models.ManyToManyField(blank=True, to='editor.SecurityControl', verbose_name='Security Control'),
        ),
        migrations.AddField(
            model_name='l3operationalthreat',
            name='SecurityPerimeter',
            field=models.ManyToManyField(blank=True, to='editor.SecurityPerimeter', verbose_name='Perimeter'),
        ),
    ]