from django.db import models

class AddBook(models.Model):

    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    pdet=models.CharField(max_length=500)
    cat=models.IntegerField()
    status=models.IntegerField()
    created_on=models.DateTimeField()
    uid=models.IntegerField()
    image=models.CharField(max_length=100000)
