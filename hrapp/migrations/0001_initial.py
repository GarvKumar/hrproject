# Generated by Django 3.1.6 on 2021-02-13 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=200)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.CharField(max_length=50)),
                ('enquirytext', models.CharField(max_length=500)),
            ],
        ),
    ]
