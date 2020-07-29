from django.db import models


class File(models.Model):
    file_name = models.CharField(max_length=1000, null=False)
