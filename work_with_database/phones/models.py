from django.db import models


class Phone(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(max_length=10)
    image = models.ImageField(max_length=100)
    release_date = models.DateField(max_length=10)
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(max_length=200,db_column=name,unique=True)

    # TODO: Добавьте требуемые поля
    pass
