from django.db import models

# Create your models here.

#class 어떻게 생성하는지 까먹지 말기

class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField('date published',null=True)

    def __str__(self):
        return self.title
    #이 꿀팁 외우기

    def summary(self):
        return self.body[:100]
