from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.title)