# Generated by Django 4.1.4 on 2022-12-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='type',
            field=models.CharField(choices=[('Standard', 'Standard'), ('Business', 'Business'), ('PRO', 'PRO'), ('Enterprise', 'Enterprise')], max_length=100),
        ),
    ]