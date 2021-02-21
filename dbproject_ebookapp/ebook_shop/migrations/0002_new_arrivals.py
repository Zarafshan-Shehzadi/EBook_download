# Generated by Django 3.1.4 on 2021-01-10 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Arrivals',
            fields=[
                ('isbn', models.CharField(db_column='ISBN', max_length=20, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=20)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('book_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='ebook_shop/images')),
            ],
        ),
    ]
