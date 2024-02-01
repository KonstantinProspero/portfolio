# Generated by Django 4.2.9 on 2024-01-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(
                    help_text='Введите текст поста', verbose_name='Текст поста')),
                ('pub_date', models.DateTimeField(
                    auto_now_add=True, verbose_name='Дата публикации')),
                ('image',
                 models.ImageField(blank=True,
                                   upload_to='projects/images/',
                                   verbose_name='Картинка')),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-pub_date',),
            },
        ),
    ]
