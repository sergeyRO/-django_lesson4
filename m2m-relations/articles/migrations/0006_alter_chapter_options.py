# Generated by Django 4.1.2 on 2022-11-02 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_chapter_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]