# Generated by Django 4.1.4 on 2022-12-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_offers', '0003_remove_joboffer_workplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='salary_from',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='salary_up_to',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
