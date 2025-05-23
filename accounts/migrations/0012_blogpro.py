# Generated by Django 5.1.4 on 2025-03-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_contactpro'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogPro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogDate', models.CharField(max_length=200, null=True)),
                ('BlogMonth', models.CharField(max_length=200, null=True)),
                ('BlogTitle', models.CharField(max_length=200, null=True)),
                ('BlogDes', models.CharField(max_length=200, null=True)),
                ('BlogUser', models.CharField(max_length=200, null=True)),
                ('BlogCmt', models.CharField(max_length=200, null=True)),
                ('BlogImage', models.ImageField(blank=True, null=True, upload_to='productImages/')),
            ],
        ),
    ]
