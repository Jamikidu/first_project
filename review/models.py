from django.contrib.auth.models import User
from django.db import models

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이
    subject = models.CharField(max_length=200)  # 제목
    content = models.TextField()  # 질문 내용
    create_date = models.DateTimeField()  # 등록일

    def __str__(self):
        return self.subject

class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content