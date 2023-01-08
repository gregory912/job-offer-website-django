# Generated by Django 4.1.4 on 2023-01-07 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_initial'),
        ('job_offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('job_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_offers.joboffer')),
            ],
        ),
    ]
