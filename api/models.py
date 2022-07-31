from djongo import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Illustrator(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    region = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class LightNovel(models.Model):
    STATUS = [
        ('Publishing', 'Publishing'),
        ('Finished', 'Finished')
    ]
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    illustration = models.URLField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, null=True) #Publising, Finished
    authors = models.ManyToManyField(Author, blank=True, null=True)
    illustrators = models.ManyToManyField(Illustrator, blank=True, null=True)
    publishers = models.ManyToManyField(Publisher, blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True,null=True)

    def __str__(self):
        return self.title

class Volume(models.Model):
    light_novel = models.ForeignKey(LightNovel, on_delete=models.CASCADE, null=False, related_name="volumes")
    name = models.CharField(max_length=100, null=False)
    illustration = models.URLField(max_length=200, null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class AlternateName(models.Model):
    name = models.CharField(max_length=100, null=False)
    light_novel = models.ForeignKey(LightNovel, on_delete=models.CASCADE, null=False, related_name="alternatenames")

    def __str__(self):
        return self.name

