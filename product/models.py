from django.db import models
from django.urls import reverse
from user.models import CustomerUser

class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.SlugField(max_length=40)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('Home:store_by_category', args=[self.slug])


class Product(models.Model):
    
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=40)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    images = models.ImageField(upload_to = 'images', null  = False, default= None)

    def __str__(self):
        return f"{self.title}, {self.category}, {self.images}"
    def get_url(self):
        return reverse('Home:product_detail', args=[self.category.slug, self.slug])




class Comment(models.Model):
    post = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete= models.CASCADE)
    body = models.CharField(max_length= 255)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return (
            f"{self.user} - "
            f"{self.post.title} "
            f"({self.date_added: %d-%m-%Y %H:%M}): "
            f"{self.body[:30]}..."
        )