# Generated by Django 3.0.6 on 2020-05-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20200514_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.FileField(upload_to='images/products'),
        ),
    ]