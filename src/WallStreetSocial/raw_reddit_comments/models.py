from django.db import models

# Create your models here.
class RawComment(models.Model):
    comment_id = models.TextField()
    comment_timestamp = models.TextField() # to be changed
    comment_body = models.TextField()
    comment_upvotes = models.IntegerField()