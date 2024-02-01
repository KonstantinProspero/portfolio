# Generated by Django 4.2.9 on 2024-02-01 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('blog',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='comments',
                                   to='blog.blog')),
            ],
        ),
    ]