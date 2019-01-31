from django.db import models

# Create your models here.
class Choice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    content_2 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    q=models.IntegerField(default=0)
    w=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
        
class Answer(models.Model):
    
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content