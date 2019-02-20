# Generated by Django 2.1.5 on 2019-02-19 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esv_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='book',
        ),
        migrations.AlterUniqueTogether(
            name='verse',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='verse',
            name='chapter',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
        migrations.DeleteModel(
            name='Verse',
        ),
    ]