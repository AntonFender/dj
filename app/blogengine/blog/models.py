from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug +  '-' + str(int(time()))


class Post(models.Model):
#Создаем столбцы в нашей БД

    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

#Когда мы в консоле выводим что-то на печать print там какой-нить объект, то python  возвращает нам объект object
#и дальше адрес. Это ненаглядно и неудобно. Поэтому обычно классы переопределяют. Метод str который отвечает за
#вывод информации об объекте. Мы использовали форматирование строк, где {} - место куда будут подставлять данные
#self.title это заголовок конкретного экземляра класса Post
    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Tag(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)