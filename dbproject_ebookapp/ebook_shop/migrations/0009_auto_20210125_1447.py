# Generated by Django 3.1.4 on 2021-01-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_shop', '0008_auto_20210125_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='favourites',
            field=models.ManyToManyField(default=None, null=True, related_name='favourite', to='ebook_shop.AuthUser'),
        ),
        migrations.AlterModelTable(
            name='wishlist',
            table=None,
        ),
    ]
