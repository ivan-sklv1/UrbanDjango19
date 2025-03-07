from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=40)
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    description = models.CharField(max_length=512)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
