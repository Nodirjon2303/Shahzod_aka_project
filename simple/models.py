from django.db import models

class language(models.Model):
    lang = models.CharField(max_length=125, null=True)

    def __str__(self):
        return self.lang

class Data(models.Model):
    name = models.CharField(max_length=120, null=True)
    age = models.FloatField(default=12)
    height = models.FloatField(default=125)
    description = models.TextField(null=True)
    status = models.BooleanField(null=True)
    lang = models.ForeignKey(language,null=True,  on_delete=models.SET_NULL)

