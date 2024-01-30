from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(
        'Текст поста',
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(
        u'Дата публикации',
        auto_now_add=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='projects/images/',
        blank=True
    )
    url = models.URLField(blank=True)
    # Аргумент upload_to указывает директорию,
    # в которую будут загружаться пользовательские файлы.

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:15]

