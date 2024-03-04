from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30) # 제목
    content = models.CharField(max_length=100) # 내용
    date = models.DateField() # 날짜

    def __str__(self):
        return self.title
