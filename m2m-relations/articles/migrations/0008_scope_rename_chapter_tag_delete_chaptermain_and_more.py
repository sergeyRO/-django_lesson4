# Generated by Django 4.1.2 on 2022-11-02 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_chapter_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article')),
            ],
        ),
        migrations.RenameModel(
            old_name='Chapter',
            new_name='Tag',
        ),
        migrations.DeleteModel(
            name='ChapterMain',
        ),
        migrations.AddField(
            model_name='scope',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.tag'),
        ),
    ]
