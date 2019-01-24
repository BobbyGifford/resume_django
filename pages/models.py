from django.db import models


class Project(models.Model):
    rank = models.IntegerField(blank=True, default=0)
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField()
    tech_used = models.CharField(max_length=300)
    live_link = models.CharField(max_length=200, blank=True)
