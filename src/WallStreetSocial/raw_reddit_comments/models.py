from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_id = models.TextField()
    comment_timestamp =
    comment_body = models.TextField()
    comment_upvotes = 