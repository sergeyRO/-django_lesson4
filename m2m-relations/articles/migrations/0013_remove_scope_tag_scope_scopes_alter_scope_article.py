# Generated by Django 4.1.2 on 2022-11-02 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_alter_scope_article_alter_scope_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='tag',
        ),
        migrations.AddField(
            model_name='scope',
            name='scopes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.tag', verbose_name='РАЗДЕЛ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope', to='articles.article'),
        ),
    ]
