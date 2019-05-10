from django.db import models


class Book(models.Model):

    title = models.CharField("Book Title", "Title", max_length=200)
    author = models.CharField("Author", "Author", max_length=100)
    year = models.PositiveSmallIntegerField("Year")
    description = models.TextField(blank=True, null=True)

    def __str__():
        return self.title
