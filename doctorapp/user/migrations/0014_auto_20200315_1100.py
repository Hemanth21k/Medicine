# Generated by Django 2.2.7 on 2020-03-15 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_item_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0013_auto_20200315_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField()),
                ('ordered_items', models.ManyToManyField(to='cart.Cart')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='history',
            field=models.ManyToManyField(to='user.History'),
        ),
    ]