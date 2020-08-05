from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
# Model to store Image retrieved from different sites
class Image(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="images_created", on_delete= models.CASCADE) # this specifies a one-to-many relationship
     title = models.CharField(max_length=200) # a title for the image
     slug = models.SlugField(max_length=200, blank=True) #  A short label that contains only letters, numbers, underscores, or hyphens to be used for building beautiful SEO-friendly URLs. 
     url = models.URLField() #  The original URL for this image. 
     image = models.ImageField(upload_to='images/%Y/%m/%d/') #  The image file. 
     description = models.TextField(blank=True) #  An optional description for the image. 
     created = models.DateField(auto_now_add=True, db_index = True) # The date and time that indicate when the object was created in the database
     users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True) # ManyToMany relationship

     def __str__(self):
         return self.title


    # this function automatically generates image slug when there is none provided.
     def save(self, *args, **kwargs):
        if not self.slug:
               self.slug = slugify(self.title)
               super().save(*args, **Kwargs)