# Generated by Django 2.2.5 on 2020-05-03 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0004_auto_20200428_0140'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='donor_name',
            field=models.CharField(max_length=50),
        ),
    ]
