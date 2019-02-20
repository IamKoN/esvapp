# Generated by Django 2.0.6 on 2018-06-03 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_auto_20180531_0944'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product'),
        ),
    ]