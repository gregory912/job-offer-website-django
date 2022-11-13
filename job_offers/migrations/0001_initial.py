# Generated by Django 4.1.3 on 2022-11-11 19:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(choices=[('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Finances', 'Finances'), ('Engineering', 'Engineering'), ('Design', 'Design'), ('HR', 'HR'), ('Consulting', 'Consulting'), ('BI & Data', 'BI & Data'), ('SEO', 'SEO'), ('PM', 'PM'), ('Media', 'Media'), ('Support', 'Support'), ('Logistic', 'Logistic'), ('Other', 'Other')], max_length=100)),
                ('workplace', models.CharField(max_length=100)),
                ('experience', models.CharField(choices=[('Internship/Junior', 'Internship/Junior'), ('Mid', 'Mid'), ('Senior', 'Senior'), ('Manager/C level', 'Manager/C level')], max_length=100)),
                ('form_of_employment', models.CharField(choices=[('Fixed-term contract', 'Fixed-term contract'), ('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Self-employment', 'Self-employment'), ('Internship employment', 'Internship employment')], max_length=100)),
                ('salary_from', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('salary_up_to', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('currency', models.CharField(choices=[('GBP', 'GBP'), ('EUR', 'EUR'), ('CHF', 'CHF'), ('USD', 'USD'), ('PLN', 'PLN')], max_length=100)),
                ('job_description', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('addres', models.CharField(max_length=200)),
                ('operationg_mode', models.CharField(choices=[('Remote work', 'Remote work'), ('Hybrid work', 'Hybrid work'), ('On site', 'On site')], max_length=100)),
                ('working_time', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Internship', 'Internship')], max_length=100)),
                ('remote_recruitment', models.BooleanField(blank=True, null=True)),
                ('information_clause', models.CharField(max_length=500)),
                ('employee_clause', models.BooleanField(default=False)),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('contact_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('skills', models.ManyToManyField(blank=True, to='employee.skill')),
                ('skills_nice_to_have', models.ManyToManyField(blank=True, related_name='skills_nice_to_have', to='employee.skill')),
                ('subscription', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employer.subscription')),
            ],
        ),
    ]
