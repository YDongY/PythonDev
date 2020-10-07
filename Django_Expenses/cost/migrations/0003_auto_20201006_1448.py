# Generated by Django 3.1.2 on 2020-10-06 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0002_auto_20201006_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '支出类型', 'verbose_name_plural': '支出类型'},
        ),
        migrations.AlterModelOptions(
            name='expenses',
            options={'ordering': ['-date'], 'verbose_name': '支出记录', 'verbose_name_plural': '支出记录'},
        ),
        migrations.AlterField(
            model_name='expenses',
            name='amount',
            field=models.FloatField(verbose_name='总支出'),
        ),
    ]