from django.db import models

# Create your models here.
class Comment():
    comment_id = models.TextField()
    comment_timestamp =
    comment_body = models.TextField()
    comment_upvotes = 