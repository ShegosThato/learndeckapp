from django.db import models
from django.conf import settings
from django.urls import reverse
from datetime import datetime

class Post(models.Model):
   title = models.CharField(max_length=50)
   slug = models.SlugField(db_index=True)
   body = models.TextField()
   date_created = models.DateTimeField(auto_now_add=True)
   post_img = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

   def get_absolute_url(self):
      return reverse('forum:post_detail', kwargs={'slug': self.post.slug})

   def __str__(self):
      return self.title
      
   class Meta:
      ordering = ('-date_created',)
      index_together = (('id', 'slug'),)

