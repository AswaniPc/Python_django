# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 07:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120, unique=True)),
                ('status', models.CharField(choices=[('Started', 'Started'), ('Abandoned', 'Abandoned'), ('Finished', 'Finished')], default='Started', max_length=120)),
                ('sub_total', models.DecimalField(decimal_places=1, default=10.99, max_digits=10)),
                ('tax_total', models.DecimalField(decimal_places=1, default=0.0, max_digits=10)),
                ('final_total', models.DecimalField(decimal_places=1, default=10.99, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('billing_address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='accounts.UserAddress')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
                ('shipping_address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='accounts.UserAddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]