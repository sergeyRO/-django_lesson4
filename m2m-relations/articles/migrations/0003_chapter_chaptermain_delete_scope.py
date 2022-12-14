# Generated by Django 4.1.2 on 2022-11-02 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articles', models.ManyToManyField(related_name='chapters', to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='articles.article')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='articles.chapter')),
            ],
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
    ]
